-- Inventory Analysis

USE supply_chain;

SELECT
    Product_Name,
    ROUND(AVG(Inventory_Level), 2) AS Average_Inventory,
    ROUND(AVG(Reorder_Level), 2) AS Average_Reorder_Level,
    Inventory_Status,
    COUNT(*) AS Number_of_Records
FROM Orders
GROUP BY Product_Name, Inventory_Status
ORDER BY Average_Inventory;
