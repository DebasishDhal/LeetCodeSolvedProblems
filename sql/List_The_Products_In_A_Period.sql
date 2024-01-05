/*
Table: Products
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table. This table contains data about the company's products.
 Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows. product_id is a foreign key (reference column) to the Products table. unit is the number of products ordered in order_date.
 Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount. Return the result table in any order.
*/

# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) as unit
FROM Products p
INNER JOIN Orders o on p.product_id = o.product_id
-- WHERE MONTH(o.order_date) = 2 AND YEAR(o.order_date) = 2020 -- 3 methods for checking date
-- WHERE o.order_date LIKE '2020-02-%'
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100

/*
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = products.merge(orders, how = 'inner', on ='product_id')
    start = pd.Timestamp(year=2020, month=2, day=1)
    end = pd.Timestamp(year=2020, month=2, day=29)
    df = df.query('@start<=order_date<=@end')
    # df = df[(df.order_date.dt.year==2020)&(df.order_date.dt.month==2)]
    df = df.groupby(['product_id','product_name'],as_index=False).agg(unit = ('unit','sum')).query('unit>=100')
    return df[['product_name','unit']]
*/
