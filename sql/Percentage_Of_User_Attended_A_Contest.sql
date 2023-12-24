-- # Write your MySQL query statement below
-- Since we want a constant to be divided by COUNT(user_id), we can call it directly without doing any joins. 
SELECT r.contest_id, ROUND(
    100*COUNT(user_id)/ (SELECT COUNT(user_id) FROM Users) -- (SELECT COUNT(user_id) FROM Users) and not (SELECT COUNT(user_id) FROM Registers) because Users has all the user_id. 
,2) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

/*
able: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.
 

Table: Register

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.
 

Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The result format is in the following example.
*/

/* Beats 93%.
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = len(users['user_id'].unique())

    df = register.groupby('contest_id').size().reset_index()
    df.columns = ['contest_id', 'percentage']
    # df['percentage'] = (100*df['percentage']/total_users).round(2) #Use this or the apply method
    df['percentage'] = df['percentage'].apply(lambda x: 100*x/total_users).round(2)

    df.sort_values(by = ['percentage','contest_id'], ascending = [False,True],inplace=True)
    print(df.columns)

    return df
*/
