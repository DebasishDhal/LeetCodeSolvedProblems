/*Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows.  customer_id is not NULL. product_key is a foreign key (reference column) to Product table.
Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table. Write a solution to report the customer ids from the Customer table that bought all the products in the Product table. Return the result table in any order. The result format is in the following example.*/

-- # Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)

/*
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_keys = product['product_key'].unique() 
    # print(type(product_keys), product_keys)

    customer = customer.groupby('customer_id', as_index=False)['product_key'].agg(lambda x: list(set(x))) #simply equating to the list is not working. It'll throw an error.
    # print(type(customer['product_key'].iloc[0]))
    df = customer[customer['product_key'].apply(lambda x: set(product_keys).issubset(x))]

    # print(customer)
    return df[['customer_id']]
*/
