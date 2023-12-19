/*
Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.
 

Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.
 

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.
*/

-- Write your MySQL query statement below
SELECT 
Visits.customer_id, COUNT(Visits.visit_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions ON
Visits.visit_id = Transactions.visit_id
WHERE 
Transactions.transaction_id IS NULL
GROUP BY 
Visits.customer_id

/*
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, on = 'visit_id', how = 'left') #So that if a visit id doesn't have a transaction_id, it'll get merged as NULL
    df = df[df['transaction_id'].isna()] #Getting all the visits with null transactions
    df = df.groupby(['customer_id'], as_index=False).agg(count_no_trans=('visit_id','nunique')) #Groupby customer_id, in place of customer_id, we want a new col called count_no_trans #which will count the number of unique visits of that customer
    return df
*/
