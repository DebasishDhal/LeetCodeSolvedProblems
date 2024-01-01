/*
Table: Products
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table. Each row of this table indicates that the price of some product was changed to a new price at some date. Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10. Return the result table in any order. The result format is in the following example.
Example 1:Input: Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output: 
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
*/


SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN 
    (SELECT DISTINCT product_id FROM Products WHERE change_date <= '2019-08-16')

UNION

SELECT product_id, new_price AS price
FROM Products 
WHERE (product_id, change_date) IN
    (SELECT product_id, max(change_date) as date FROM Products
    WHERE change_date <= '2019-08-16' GROUP BY product_id)



/* #My code, smoewhere in the mean range. Someone condensed this to a 2 line code.
import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products['before_date'] = products['change_date'] <= pd.Timestamp('2019-08-16')
    no_change = products.groupby('product_id')['before_date'].all().loc[lambda x: ~x].index
    changed = products[products['before_date'] == True]
    max_date_indices = changed.groupby('product_id')['change_date'].idxmax()
    result_changed = changed[['product_id','new_price']].loc[max_date_indices]
    result_no_changed = pd.DataFrame({'product_id': no_change, 'new_price':[10]*len(no_change)})
    result =  pd.concat([result_changed, result_no_changed], axis=0)[['product_id','new_price']]
    result.columns = ['product_id','price']
    result = result.drop_duplicates(subset=['product_id'],keep='first')
    return result

#Optimized
def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    temp_df = products[products['change_date']<='2019-08-16'].sort_values(by='change_date', ascending=False)
    temp_df = temp_df.groupby('product_id')['new_price'].first().to_frame()
    res_df = pd.Series(products.product_id.unique()).to_frame('product_id').merge(temp_df, how='left', on='product_id').fillna(10)
    res_df.columns = ['product_id', 'price']
    return res_df

*/
