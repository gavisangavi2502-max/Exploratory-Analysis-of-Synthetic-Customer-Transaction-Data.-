import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Generate synthetic dataset
n = 500
data = pd.DataFrame({
    'TransactionID': range(1, n+1),
    'CustomerSegment': np.random.choice(['A','B','C'], n),
    'PurchaseAmount': np.random.normal(200, 50, n).round(2),
    'TransactionDate': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0,365,n), unit='D')
})

# Data inspection
print(data.info())
print(data.head())

# Descriptive statistics
stats = data.groupby('CustomerSegment')['PurchaseAmount'].agg(['mean','median','std'])
print(stats)

# Visualizations
plt.hist(data['PurchaseAmount'])
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.savefig('/mnt/data/histogram.png')
plt.clf()

stats.plot(kind='bar')
plt.title("Average Purchase Amount by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Value")
plt.savefig('/mnt/data/bar_chart.png')
