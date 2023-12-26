-- # Write your MySQL query statement below. Beats 56%. This problem was quite good. Proper balance between my capability and additional effort required.

SELECT 
    ROUND( COUNT( DISTINCT player_id )/ ( SELECT COUNT(DISTINCT player_id) FROM Activity ), 2 ) 
    AS fraction
FROM 
    Activity
WHERE 
    (player_id, DATE_ADD(event_date, INTERVAL -1 DAY)) IN  --  DATE_ADD(Today, INTERVAL 1 DAY) = Tomorrow. Similarly DATE_SUB exists.
(
    SELECT 
        player_id, MIN(event_date)
    FROM 
        Activity
    GROUP BY 
        player_id
)

/*
Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table. This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    distinct_players = len(activity['player_id'].unique())

    first_login = activity.groupby('player_id', as_index=False)['event_date'].min()

    first_login_shift = activity.copy()
    first_login_shift['event_date'] = first_login_shift['event_date'] - pd.Timedelta(days=1)

    df = first_login_shift.merge(first_login, on = ['player_id','event_date'], how='inner')
    percentage = len(df)/distinct_players

    return pd.DataFrame({'fraction':[percentage]}).round(2)
*/

