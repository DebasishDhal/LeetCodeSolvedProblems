/*
Table: Queries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 
We define query quality as: The average of the ratio between query rating and its position.
We also define poor query percentage as: The percentage of all queries with rating less than 3.
Write a solution to find each query_name, the quality and poor_query_percentage. Both quality and poor_query_percentage should be rounded to 2 decimal places. Return result table in any order.
*/
-- # Write your MySQL query statement below BEats 95%
SELECT 
query_name,
ROUND( AVG( rating/position ), 2 ) as quality, 
ROUND( 100 * SUM(CASE WHEN rating<3 THEN 1 ELSE 0 END) / COUNT(*), -- For every group it tells what percentage of rows have less than 3 rating. You can replace this with AVG(CASE WHEN rating<3 THEN 1 ELSE 0 END). No need for count(*)
  2 ) AS poor_query_percentage 
FROM Queries
GROUP BY query_name
HAVING query_name IS NOT Null -- We don't want Null query to be taken as a valid query and thus grouped accordingly. Having is used after groupined, you can't use where after grouping.

/* This code is working on all testcases except the damned last testcase. And leetcode devs want us to manually find out the difference between expected and actual tabular output.

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries.dropna(subset=['query_name'],inplace=True)

    queries['qual_pos'] = queries['rating']/(queries['position'])

    queries['poor_query_percentage'] = (queries['rating'] < 3) * 100 #Clever way

    queries = queries.groupby('query_name', as_index=False)[['qual_pos','poor_query_percentage']].mean().round(2)

    # queries = queries.groupby('query_name', as_index=False).agg( #Another way of aggregating
    #     {'qual_pos':'mean','poor_query_percentage':'mean'}
    #     ).reset_index().round(2)

    queries.columns = ['query_name', 'quality','poor_query_percentage']

    return queries
*/

