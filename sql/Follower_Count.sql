/*
Table: Followers

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.
 

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by user_id in ascending order.

The result format is in the following example.
*/

-- # Write your MySQL query statement below
SELECT user_id,
COUNT(follower_id) as followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC

/*
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return followers.groupby('user_id')['follower_id'].count().reset_index().rename(columns = {'follower_id':'followers_count'})
    #groupby return a series (and not a dataframe), we use follower_id and count to count the occurences in follower_id col. We use reset_index because col names are destroyed in grouping.
#Once reset_index is done, we rename the column and that's it.
*/
