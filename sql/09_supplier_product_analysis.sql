-- Supplier + Product Delay Analysis

USE supply_chain;

SELECT
    Supplier_Name,
    Product_Name,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN Delivery_Status = 'Delayed' THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM Orders
GROUP BY Supplier_Name, Product_Name
HAVING Delayed_Orders > 0
ORDER BY Delayed_Orders DESC, Average_Delay DESC;

-- Top 10 problematic supplier-product combinations

SELECT
    Supplier_Name,
    Product_Name,
    COUNT(*) AS Delayed_Orders,
    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delay
FROM Orders
WHERE Delivery_Status = 'Delayed'
GROUP BY Supplier_Name, Product_Name
ORDER BY Delayed_Orders DESC
LIMIT 10;
