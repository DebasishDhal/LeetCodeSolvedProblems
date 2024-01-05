/*
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table. This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase. Return the result table ordered by user_id.
*/

-- # Write your MySQL query statement below
SELECT user_id, CONCAT( UPPER( SUBSTR(name,1,1) ), LOWER( SUBSTR(name, 2) ) ) AS name
FROM Users
ORDER BY user_id

/*
import pandas as pd

# def capitalizer(row):
#     name = row['name']
#     name = name[:1].upper() + name[1:].lower()
#     row['name'] = name
#     return row

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    # users = users.apply(capitalizer, axis=1)
    users.sort_values(by='user_id',inplace=True)
    return users
*/
