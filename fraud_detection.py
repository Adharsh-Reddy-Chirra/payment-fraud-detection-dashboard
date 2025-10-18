import pandas as pd
import sqlite3
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Load transactions
conn = sqlite3.connect('transactions.db')
data = pd.read_sql_query("SELECT * FROM transactions", conn)
conn.close()

# Encode text columns into numbers
le_loc = LabelEncoder()
le_method = LabelEncoder()
data['location_enc'] = le_loc.fit_transform(data['location'])
data['method_enc'] = le_method.fit_transform(data['method'])

# Select features to use for fraud detection
features = data[['amount', 'location_enc', 'method_enc', 'device_id']]

# Train Isolation Forest to find anomalies
model = IsolationForest(n_estimators=100, contamination=0.03, random_state=42)
data['fraud_pred'] = model.fit_predict(features)

# Convert model output to 1 for fraud, 0 for normal
data['fraud_pred'] = data['fraud_pred'].map({1: 0, -1: 1})

# Save predictions
data.to_csv('fraud_results.csv', index=False)

print("Fraud detection done! Results saved to fraud_results.csv")
