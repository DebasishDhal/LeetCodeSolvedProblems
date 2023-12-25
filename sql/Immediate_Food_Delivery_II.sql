/*
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The result format is in the following example.

 

Example 1:

Input: 
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
Output: 
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
*/

# Write your MySQL query statement below

-- In the subquery we return customer_id and order_date of earliest order of each customer.
-- Then we match customer_id and order_date with output of that subquery. After that we count
-- how many rows have same order and customer_pref_delivery date. 

SELECT ROUND(
    100 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(DISTINCT(customer_id)) -- Replacing COUNT(*) with COUNT(DISTINCT(customer_id)) greately speeds up the execution.
    ,2)
AS immediate_percentage
FROM Delivery 
WHERE (customer_id, order_date ) -- If you are using a subquery, you have to use a WHERE to match something with the output of subquery.
IN (
    SELECT
        customer_id,
        MIN(order_date) AS earliest_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
) 

/*
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery.sort_values(by = ['order_date'],inplace=True)
    delivery.drop_duplicates(subset = ['customer_id'], keep = 'first', inplace=True)

    delivery['same_date'] = (delivery['order_date'] == delivery['customer_pref_delivery_date'])

    immediate_percentage = 100*delivery['same_date'].sum()/len(delivery)
    # print(immediate_percentage)

    return pd.DataFrame({'immediate_percentage':[immediate_percentage]}).round(2)
*/

