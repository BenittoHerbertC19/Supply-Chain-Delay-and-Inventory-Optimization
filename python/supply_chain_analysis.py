import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# SUPPLY CHAIN ANALYTICS PROJECT
# ==========================================

# Load dataset
file_path = "../data/supply_chain_dataset_2000.xlsx"
df = pd.read_excel(file_path)

print("==========================================")
print("SUPPLY CHAIN ANALYTICS PROJECT")
print("==========================================")
print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# DATA QUALITY CHECK
# ==========================================

print("\n==========================================")
print("DATA QUALITY CHECK")
print("==========================================")

print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())


# ==========================================
# DATE CONVERSION
# ==========================================

date_columns = [
    'Order_Date',
    'Shipping_Date',
    'Expected_Delivery_Date',
    'Actual_Delivery_Date'
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column])

print("Date columns converted successfully.")


# ==========================================
# SUPPLIER PERFORMANCE
# ==========================================

supplier_analysis = df.groupby(
    ['Supplier_ID', 'Supplier_Name']
).agg(
    Total_Orders=('Order_ID', 'count'),
    Delayed_Orders=('Delivery_Status', lambda x: (x == 'Delayed').sum()),
    Avg_Delay_Days=('Delivery_Delay_Days', 'mean'),
    On_Time_Percentage=('Delivery_Status', lambda x: (x == 'On Time').mean() * 100)
).reset_index()

print("\nSupplier Performance:")
print(supplier_analysis)


# ==========================================
# PRODUCT PERFORMANCE
# ==========================================

product_analysis = df.groupby(
    ['Product_ID', 'Product_Name', 'Category']
).agg(
    Total_Orders=('Order_ID', 'count'),
    Total_Quantity=('Quantity', 'sum'),
    Avg_Delay_Days=('Delivery_Delay_Days', 'mean'),
    On_Time_Percentage=('Delivery_Status', lambda x: (x == 'On Time').mean() * 100)
).reset_index()

print("\nProduct Performance:")
print(product_analysis)


# ==========================================
# WAREHOUSE PERFORMANCE
# ==========================================

warehouse_analysis = df.groupby(
    ['Warehouse_ID', 'Warehouse_Name']
).agg(
    Total_Orders=('Order_ID', 'count'),
    Total_Quantity=('Quantity', 'sum'),
    Avg_Delay_Days=('Delivery_Delay_Days', 'mean'),
    On_Time_Percentage=('Delivery_Status', lambda x: (x == 'On Time').mean() * 100)
).reset_index()

print("\nWarehouse Performance:")
print(warehouse_analysis)


# ==========================================
# OVERALL KPIs
# ==========================================

total_orders = len(df)
total_quantity = df['Quantity'].sum()
average_delay = df['Delivery_Delay_Days'].mean()
overall_on_time = (df['Delivery_Status'] == 'On Time').mean() * 100

print("\n==========================================")
print("OVERALL SUPPLY CHAIN KPIs")
print("==========================================")

print("Total Orders:", total_orders)
print("Total Quantity:", total_quantity)
print("Average Delivery Delay:", round(average_delay, 2), "days")
print("Overall On-Time Delivery:", round(overall_on_time, 2), "%")


# ==========================================
# MONTHLY PERFORMANCE
# ==========================================

df['Order_Month'] = df['Order_Date'].dt.to_period('M').astype(str)

monthly_analysis = df.groupby('Order_Month').agg(
    Total_Orders=('Order_ID', 'count'),
    Total_Quantity=('Quantity', 'sum'),
    Avg_Delay_Days=('Delivery_Delay_Days', 'mean'),
    On_Time_Percentage=('Delivery_Status', lambda x: (x == 'On Time').mean() * 100)
).reset_index()

print("\nMonthly Performance:")
print(monthly_analysis)


# ==========================================
# CHART 1: SUPPLIER PERFORMANCE
# ==========================================

plt.figure(figsize=(10, 6))

plt.bar(
    supplier_analysis['Supplier_Name'],
    supplier_analysis['On_Time_Percentage']
)

plt.title('Supplier On-Time Performance')
plt.xlabel('Supplier')
plt.ylabel('On-Time Delivery (%)')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig('../dashboard/supplier_on_time_performance.png', dpi=300)
plt.close()


# ==========================================
# CHART 2: PRODUCT DEMAND
# ==========================================

plt.figure(figsize=(10, 6))

plt.barh(
    product_analysis['Product_Name'],
    product_analysis['Total_Quantity']
)

plt.title('Product Demand by Quantity')
plt.xlabel('Total Quantity')
plt.ylabel('Product')
plt.tight_layout()

plt.savefig('../dashboard/product_demand.png', dpi=300)
plt.close()


# ==========================================
# CHART 3: MONTHLY ON-TIME PERFORMANCE
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_analysis['Order_Month'],
    monthly_analysis['On_Time_Percentage'],
    marker='o'
)

plt.title('Monthly On-Time Delivery Performance')
plt.xlabel('Month')
plt.ylabel('On-Time Delivery (%)')
plt.xticks(rotation=45)
plt.ylim(70, 100)
plt.grid(True)
plt.tight_layout()

plt.savefig('../dashboard/monthly_on_time_performance.png', dpi=300)
plt.close()


# ==========================================
# KEY INSIGHTS
# ==========================================

best_supplier = supplier_analysis.loc[
    supplier_analysis['On_Time_Percentage'].idxmax()
]

worst_supplier = supplier_analysis.loc[
    supplier_analysis['On_Time_Percentage'].idxmin()
]

highest_demand_product = product_analysis.loc[
    product_analysis['Total_Quantity'].idxmax()
]

best_warehouse = warehouse_analysis.loc[
    warehouse_analysis['On_Time_Percentage'].idxmax()
]

worst_warehouse = warehouse_analysis.loc[
    warehouse_analysis['On_Time_Percentage'].idxmin()
]

print("\n==========================================")
print("KEY INSIGHTS")
print("==========================================")

print(
    "Best Supplier:",
    best_supplier['Supplier_Name'],
    "-",
    round(best_supplier['On_Time_Percentage'], 2),
    "%"
)

print(
    "Worst Supplier:",
    worst_supplier['Supplier_Name'],
    "-",
    round(worst_supplier['On_Time_Percentage'], 2),
    "%"
)

print(
    "Highest-Demand Product:",
    highest_demand_product['Product_Name'],
    "-",
    highest_demand_product['Total_Quantity'],
    "units"
)

print(
    "Best Warehouse:",
    best_warehouse['Warehouse_Name'],
    "-",
    round(best_warehouse['On_Time_Percentage'], 2),
    "%"
)

print(
    "Worst Warehouse:",
    worst_warehouse['Warehouse_Name'],
    "-",
    round(worst_warehouse['On_Time_Percentage'], 2),
    "%"
)

print("\nAnalysis completed successfully!")