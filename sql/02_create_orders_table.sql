-- Create the main Orders table

USE supply_chain;

DROP TABLE IF EXISTS Orders;

CREATE TABLE Orders (
    Order_ID VARCHAR(20),
    Supplier_ID VARCHAR(20),
    Supplier_Name VARCHAR(100),
    Supplier_City VARCHAR(50),
    Product_ID VARCHAR(20),
    Product_Name VARCHAR(100),
    Category VARCHAR(50),
    Warehouse_ID VARCHAR(20),
    Warehouse_Name VARCHAR(100),
    Order_Date DATE,
    Shipping_Date DATE,
    Expected_Delivery_Date DATE,
    Actual_Delivery_Date DATE,
    Quantity INT,
    Unit_Cost DECIMAL(10,2),
    Total_Order_Value DECIMAL(12,2),
    Transportation_Cost DECIMAL(10,2),
    Lead_Time_Days INT,
    Delivery_Delay_Days INT,
    Delivery_Status VARCHAR(30),
    Inventory_Level INT,
    Reorder_Level INT,
    Inventory_Status VARCHAR(30),
    Monthly_Demand_Estimate INT,
    Supplier_Performance_Pct DECIMAL(5,2)
);
