/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
Find all numbers that appear at least three times consecutively. Return the result table in any order.
The result format is in the following example.
*/

-- # Write your MySQL query statement below
WITH combined AS (
    SELECT num, 
    LEAD(num,1) OVER() num_shift1,
    LEAD(num,2) OVER() num_shift2
    FROM Logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM combined
WHERE num = num_shift1 AND num = num_shift2

/*
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['num_shift1'] = logs['num'].shift(1)
    logs['num_shift2'] = logs['num'].shift(2)
    logs = logs[ (logs['num']==logs['num_shift1']) & (logs['num']==logs['num_shift2'])]
    logs=logs.drop_duplicates(subset=['num'])
    return logs[['num']].rename(columns = {'num':'ConsecutiveNums'})
*/
