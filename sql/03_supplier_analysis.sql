-- Supplier Performance Analysis

USE supply_chain;

SELECT
    Supplier_Name,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN Delivery_Status = 'Delayed' THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay,
    ROUND(AVG(Supplier_Performance_Pct), 2) AS Performance_Percent
FROM Orders
GROUP BY Supplier_Name
ORDER BY Delayed_Orders DESC;

-- Supplier with the highest number of delayed orders

SELECT
    Supplier_Name,
    COUNT(*) AS Delayed_Orders
FROM Orders
WHERE Delivery_Status = 'Delayed'
GROUP BY Supplier_Name
ORDER BY Delayed_Orders DESC
LIMIT 1;
