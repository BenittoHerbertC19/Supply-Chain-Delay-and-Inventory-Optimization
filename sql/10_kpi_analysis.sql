-- Overall Supply Chain KPIs

USE supply_chain;

SELECT
    COUNT(*) AS Total_Orders,

    SUM(CASE
        WHEN Delivery_Status = 'Delayed' THEN 1
        ELSE 0
    END) AS Delayed_Orders,

    SUM(CASE
        WHEN Delivery_Status = 'On Time' THEN 1
        ELSE 0
    END) AS On_Time_Orders,

    ROUND(
        100 * SUM(CASE
            WHEN Delivery_Status = 'On Time' THEN 1
            ELSE 0
        END) / COUNT(*), 2
    ) AS On_Time_Percentage,

    ROUND(AVG(Delivery_Delay_Days), 2) AS Average_Delivery_Delay,

    ROUND(SUM(Transportation_Cost), 2) AS Total_Transportation_Cost,

    ROUND(AVG(Inventory_Level), 2) AS Average_Inventory
FROM Orders;
