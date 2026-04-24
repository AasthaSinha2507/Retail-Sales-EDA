# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load dataset
df = pd.read_csv("sales_data.csv")

print("First 5 rows:")
print(df.head())

# 3. Data Cleaning
print("\nMissing values:")
print(df.isnull().sum())

df.dropna(inplace=True)

print("\nDuplicates:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# 4. Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# 5. Convert Date column (IMPORTANT)
df['Date'] = pd.to_datetime(df['Date'])

# 6. Time Series Analysis
sales_trend = df.groupby('Date')['Sales'].sum()

plt.figure()
sales_trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

# 7. Sales by Product
plt.figure()
sns.barplot(x='Product', y='Sales', data=df)
plt.xticks(rotation=90)
plt.title("Sales by Product")
plt.show()

# 8. Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()