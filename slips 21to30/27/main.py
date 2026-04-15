import pandas as pd
import random
import csv

# 1. Generate random transaction data
data = []
for i in range(1, 101):
    item_price = round(random.uniform(10.0, 100.0), 2)
    quantity = random.randint(1, 10)
    data.append([i, random.randint(1, 10), item_price, quantity])

# 2. Save to CSV
with open('transactions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["T_ID", "Customer_ID", "Price", "Quantity"])
    writer.writerows(data)

# 3. Process with Pandas
df = pd.read_csv('transactions.csv')

# Calculate sales per row
df['Sales'] = df['Price'] * df['Quantity']

# Group by Customer ID and sum sales
total_sales = df.groupby('Customer_ID')['Sales'].sum().reset_index()

print("Total Sales per Customer:")
print(total_sales)