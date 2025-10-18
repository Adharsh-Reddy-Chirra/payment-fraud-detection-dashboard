# 🚨 Payment Fraud Detection Dashboard

An end-to-end interactive dashboard built with Python, SQL, machine learning, and Streamlit to detect, analyze, and visualize payment fraud patterns. Designed to showcase data engineering, fraud analytics, and visualization.

---

## 🔍 What It Does

- Simulates realistic payment transaction data with fraud labeling  
- Implements an Isolation Forest ML model to identify fraudulent transactions  
- Provides interactive filtering by country and payment method  
- Displays advanced visualizations:  
  - Fraud trend over time (line chart)  
  - Heatmap of fraud intensity by hour and day  
  - Fraud count by location (clear horizontal bar chart)  
  - Average transaction amount by fraud status (simple bar chart)  
- Highlights flagged frauds with color-coded amounts for easy prioritization


## 📸 Dashboard Preview
Link to Interactive Dashoard: https://payment--fraud-detection.streamlit.app/

<img width="1592" height="877" alt="fraud trend" src="https://github.com/user-attachments/assets/fba77292-429d-46d2-8639-6b375fde6fa2" />


*Note: The image above shows the interactive Streamlit dashboard with filters and visualizations.*


## 📂 Files Included

- `database_setup.py` – Script to simulate and store transaction data in SQLite  
- `fraud_detection.py` – ML model to detect fraud and output results  
- `dashboard_app.py` – Streamlit application for interactive data visualization  
- `fraud_results.csv` – Sample output data file  
- `requirements.txt` – Python dependencies  


## 🧠 Skills Demonstrated

- Data engineering with SQL and pandas  
- Anomaly detection using Isolation Forest  
- Interactive, user-friendly dashboard development with Streamlit  
- Professional-grade data visualization with Plotly and Matplotlib  
- Focus on Trust & Safety in payment systems

## 🚀 How to Run

1. Clone the repository  
2. Install dependencies:  

pip install -r requirements.txt

3. Generate simulated transaction data:  

python database_setup.py

4. Run fraud detection model:  

python fraud_detection.py

5. Launch the dashboard:  

streamlit run dashboard_app.py

6. Explore and interact with the dashboard to analyze fraud patterns.

   
