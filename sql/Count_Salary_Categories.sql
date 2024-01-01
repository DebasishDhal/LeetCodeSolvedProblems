/*
Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
*/

-- # Write your MySQL query statement below
SELECT "Low Salary" as category,
    SUM(income<20000) as accounts_count -- Notice the very important difference between sum vs count. Count counts all non-null rows, while sum just sums over. income<20000 returns -- --boolean 1 and 0 which are summed to count number of rows.
FROM Accounts

UNION

SELECT "High Salary" as category,
    SUM(income>50000) as accounts_count
FROM Accounts

UNION

SELECT "Average Salary" as category,
    SUM(income>=20000 AND income<=50000) as accounts_count
FROM Accounts

/*
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # accounts['category'] = accounts.apply(lambda row: 'Low Salary' if row['income']<20000 else
    #                                 'Average Salary' if (20000 <= row['income'] <= 50000)else                                 'High Salary' if row['income']>50000 
    #                                 else 'Undefined', axis=1) #This took too much time.

    return pd.DataFrame(
        {
            'category':['Low Salary','Average Salary','High Salary'],
            'accounts_count':[  len(accounts[accounts['income']<20000 ]),
                            len(accounts[ (20000<=accounts['income'])& (accounts['income']<=50000) ]),
                            len(accounts[accounts['income']>50000 ]) ]
            
        }
    )

*/
