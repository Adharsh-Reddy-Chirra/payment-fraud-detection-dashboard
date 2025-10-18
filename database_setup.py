import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import random

np.random.seed(42)  # Fix randomness for consistency

n = 10000  # number of transactions

transaction_ids = list(range(1, n+1))
amounts = np.random.gamma(2.0, 300, n).round(2)  # random payment amounts
locations = np.random.choice(['USA', 'India', 'Germany', 'Japan', 'UK'], n)
methods = np.random.choice(['Credit Card', 'Debit Card', 'UPI', 'Wire', 'Crypto'], n)
device_ids = np.random.randint(1000, 9999, n)
timestamps = [datetime.now() - timedelta(minutes=random.randint(0, 60000)) for _ in range(n)]

# Flag 3% as fraud and modify their values
fraud_flags = np.random.choice([0, 1], n, p=[0.97, 0.03])
for i in range(n):
    if fraud_flags[i] == 1:
        if random.random() > 0.5:
            amounts[i] *= np.random.uniform(3, 10)  # unusually large
        else:
            locations[i] = np.random.choice(['Russia', 'Nigeria', 'Vietnam', 'Ukraine'])
        device_ids[i] = np.random.randint(9990, 9999)  # suspicious device ID range

data = pd.DataFrame({
    'transaction_id': transaction_ids,
    'amount': amounts,
    'location': locations,
    'method': methods,
    'device_id': device_ids,
    'timestamp': timestamps,
    'is_fraud': fraud_flags
})

# Save to a SQLite database
conn = sqlite3.connect('transactions.db')
data.to_sql('transactions', conn, index=False, if_exists='replace')
conn.close()

print("Database with transactions created!")
