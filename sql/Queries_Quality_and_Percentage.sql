/*Table: Transactions
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table. The table has information about incoming transactions. The state column is an enum of type ["approved", "declined"].
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
Return the result table in any order. The query result format is in the following example.

Example 1: Input:  Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output: 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
*/

-- # Write your MySQL query statement below. This was good to write, building one column after one.
SELECT 
DATE_FORMAT(trans_date, '%Y-%m') as month,                                           -- Date is available in YYYY-MM-DD format, we just want the YYYY-MM format.
country, 
COUNT(*) as trans_count,                                                             -- Count how many transactions were there for every grouping 
SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) as approved_count,               -- Count total number of successful transactions for every grouping
-- SUM(IF(state = 'approved',1,0)) can also be used            
SUM(amount) as trans_total_amount,                                                   -- Count total transaction amount for every grouping
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 end) as approved_total_amount    -- Count total successful transaction amount for every grouping
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country                                   -- We group by country and YYYY-MM


/*
import pandas as pd
import datetime
import numpy as np

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # transactions['trans_date'] = pd.to_datetime(transactions['trans_date']) #This is not required as the trans_date is already in datetime format.

    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m") #Converting into YYYY-MM format.
    transactions['approved'] = transactions.apply(lambda row: row['amount'] if row['state'] == 'approved' else np.nan, axis=1) #If approved, then put the amount, else NaN

    df =  transactions.groupby(['month', 'country'], dropna= False).agg( #dropna is default True, I didn't know, that's why there was one null row missing in the output.
        trans_count=('state', 'count'), 
        approved_count=('approved', 'count'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('approved', 'sum')
    ).reset_index()

    return df


*/
