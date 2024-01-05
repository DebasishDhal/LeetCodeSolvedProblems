/*
able Activities:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold in a market.
 

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by sell_date.
*/


-- # Write your MySQL query statement below
SELECT 
    sell_date, 
    COUNT(DISTINCT product) as num_sold, 
    GROUP_CONCAT(DISTINCT product) as products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date

/*
| sell_date  | product    |
| ---------- | ---------- |
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |

| sell_date  | num_sold | products                     |
| ---------- | -------- | ---------------------------- |
| 2020-05-30 | 3        | Basketball,Headphone,T-Shirt | #Alphabetically sorted and concatenated group members
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
*/

/*import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby(['sell_date'],as_index=False).agg(
        num_sold = ('product','nunique'),
        products=( 'product', lambda x: ','.join( sorted(x.unique()) ) )
    ).sort_values(by=['sell_date'])

    return df
*/
