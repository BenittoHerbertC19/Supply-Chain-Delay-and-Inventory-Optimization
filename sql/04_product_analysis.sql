-- Product Delay Analysis

USE supply_chain;

SELECT
    Product_Name,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN Delivery_Status = 'Delayed' THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM Orders
GROUP BY Product_Name
ORDER BY Delayed_Orders DESC;
