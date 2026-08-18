-- Transportation Cost Analysis

USE supply_chain;

SELECT
    Supplier_Name,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Transportation_Cost), 2) AS Total_Transport_Cost,
    ROUND(AVG(Transportation_Cost), 2) AS Average_Transport_Cost
FROM Orders
GROUP BY Supplier_Name
ORDER BY Total_Transport_Cost DESC;
