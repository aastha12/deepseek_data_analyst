import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Data
print("Loading Walmart data...")
data_path = './data/Walmart.csv'
df = pd.read_csv(data_path)

# Data Quality Check
print("\nData Quality Check:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)

# Create Output Directories if they don't exist
os.makedirs('./analysis_output/plots', exist_ok=True)
os.makedirs('./analysis_output', exist_ok=True)

# Visualization 1: Weekly Sales Trend
plt.figure(figsize=(10,6))
sns.lineplot(x='Date', y='Weekly_Sales', data=df)
plt.title('Weekly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.savefig('./analysis_output/plots/weekly_sales_trend.png')
plt.close()

# Visualization 2: Impact of Holidays on Sales
holiday_sales = df.groupby('Holiday_Flag')['Weekly_Sales'].sum()
plt.figure(figsize=(8,6))
sns.barplot(x=holiday_sales.index, y=holiday_sales.values)
plt.title('Impact of Holidays on Sales')
plt.xlabel('Holiday Flag')
plt.ylabel('Total Sales')
plt.savefig('./analysis_output/plots/holiday_impact.png')
plt.close()

# Visualization 3: Correlation Matrix
corr_matrix = df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.savefig('./analysis_output/plots/correlation_matrix.png')
plt.close()

# Business Insights
correlations = df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()['Weekly_Sales']
print("\nCorrelations with Weekly Sales:")
print(correlations)

# Identify Underperforming Store
store_sales = df.groupby('Store')['Weekly_Sales'].sum()
underperforming_store = store_sales.idxmin()
print("\nUnderperforming Store:")
print(underperforming_store)

# Operational Efficiency Opportunity
print("\nOperational Efficiency Opportunity:")
print("Opportunity: Optimize Inventory Turnover through Cross-docking")

# Action Plan
action_plan = """Action Plan:
1. Immediate Actions (Next 90 Days):
   a. Implement EDLP (Every Day Low Prices) Strategy to boost same-store sales growth.
   b. Optimize Inventory Turnover Ratio by improving cross-docking efficiency.

2. Strategic Initiative (6-12 Months):
   a. Invest in Data Analytics to better forecast sales and reduce logistics costs.
"""

# Save Results to File
with open('./analysis_output/results.txt', 'w') as f:
    f.write("Walmart Retail Data Analysis Results\n")
    f.write("\nData Quality Check:\n")
    f.write(str(df.head()) + "\n")
    f.write(str(df.isnull().sum()) + "\n")
    f.write(str(df.dtypes) + "\n\n")
    f.write("Correlations with Weekly Sales:\n")
    f.write(str(correlations) + "\n\n")
    f.write("Underperforming Store:\n")
    f.write(str(underperforming_store) + "\n\n")
    f.write("Operational Efficiency Opportunity:\n")
    f.write("Opportunity: Optimize Inventory Turnover through Cross-docking\n\n")
    f.write(action_plan)

print("Analysis completed successfully. Results saved to './analysis_output/results.txt'")