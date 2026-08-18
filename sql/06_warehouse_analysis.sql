-- Warehouse Performance Analysis

USE supply_chain;

SELECT
    Warehouse_Name,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN Delivery_Status = 'Delayed' THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay,
    ROUND(SUM(Transportation_Cost), 2) AS Total_Transportation_Cost
FROM Orders
GROUP BY Warehouse_Name
ORDER BY Delayed_Orders DESC;
