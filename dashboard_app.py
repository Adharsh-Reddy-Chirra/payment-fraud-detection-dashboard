import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Payment Fraud Detection Dashboard")

# Load data
data = pd.read_csv('fraud_results.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['date'] = data['timestamp'].dt.date
data['hour'] = data['timestamp'].dt.hour
data['day_of_week'] = data['timestamp'].dt.day_name()

# Sidebar filters
countries = st.sidebar.multiselect("Select Countries:", options=data['location'].unique(), default=data['location'].unique())
methods = st.sidebar.multiselect("Select Payment Methods:", options=data['method'].unique(), default=data['method'].unique())

# Filter data
filtered = data[(data['location'].isin(countries)) & (data['method'].isin(methods))]

# Show metrics
st.metric("Total Transactions", len(filtered))
st.metric("Detected Frauds", int(filtered['fraud_pred'].sum()))
st.metric("Fraud Percentage", f"{100 * filtered['fraud_pred'].mean():.2f}%")

# Trend Line: Fraud Count Over Time
st.subheader("Fraud Trend Over Time")
daily_fraud = filtered.groupby('date')['fraud_pred'].sum().reset_index()
fig_trend = px.line(daily_fraud, x='date', y='fraud_pred', markers=True, title='Daily Fraudulent Transactions')
st.plotly_chart(fig_trend, use_container_width=True)

# Heatmap: Fraud by Hour and Day of Week
st.subheader("Fraud Heatmap by Hour and Day of Week")
heatmap_data = filtered.pivot_table(index='hour', columns='day_of_week', values='fraud_pred', aggfunc='sum').fillna(0)
# Reorder days if needed
ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap_data = heatmap_data[ordered_days]
fig_heatmap = px.imshow(heatmap_data,
                       labels=dict(x="Day of Week", y="Hour of Day", color="Fraud Count"),
                       x=heatmap_data.columns,
                       y=heatmap_data.index,
                       color_continuous_scale='Reds',
                       aspect="auto",
                       title="Fraud Counts by Hour and Day of Week")
st.plotly_chart(fig_heatmap, use_container_width=True)

# Fraud Count by Location 
st.subheader("Fraud Count by Location")

# Prepare data: sum frauds by location
fraud_by_location = filtered[filtered['fraud_pred'] == 1].groupby('location').size().reset_index(name='fraud_count')

# Sort ascending
fraud_by_location = fraud_by_location.sort_values(by='fraud_count', ascending=True)

# Plot horizontal bar chart with teal color
fig_location = px.bar(fraud_by_location, 
                      x='fraud_count', 
                      y='location', 
                      orientation='h',
                      labels={'fraud_count': 'Fraud Count', 'location': 'Location'},
                      title='Fraud Counts by Location',
                      color_discrete_sequence=['#008080'])  # Teal

st.plotly_chart(fig_location, use_container_width=True)


# Transaction Amount Distribution by Fraud Status 
st.subheader("Average Transaction Amount by Fraud Status")

avg_amounts = filtered.groupby('fraud_pred')['amount'].mean().reset_index()
avg_amounts['fraud_pred'] = avg_amounts['fraud_pred'].map({0: 'Not Fraud', 1: 'Fraud'})

fig_bar = px.bar(avg_amounts, x='fraud_pred', y='amount',
                 labels={'fraud_pred': 'Fraud Status', 'amount': 'Average Transaction Amount'},
                 color='fraud_pred', color_discrete_map={'Not Fraud': 'green', 'Fraud': 'red'},
                 title='Average Transaction Amount Comparison')

st.plotly_chart(fig_bar, use_container_width=True)



# Table of flagged frauds
st.subheader("Flagged Fraudulent Transactions")

flagged = filtered[filtered['fraud_pred'] == 1]

# Use matplotlib colormap 'YlOrRd' for background gradient on 'amount'
styled_flagged = flagged.style.background_gradient(cmap='YlOrRd', subset=['amount']).format({'amount': '${:,.2f}'})

st.dataframe(styled_flagged)


