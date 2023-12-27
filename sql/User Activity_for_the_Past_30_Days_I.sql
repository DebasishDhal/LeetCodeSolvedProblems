'''
Table: Activity
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows. The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website.  Note that each session belongs to exactly one user.
Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.
'''

-- # Write your MySQL query statement below
SELECT activity_date as day,
COUNT( DISTINCT user_id) as active_users
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30 and DATEDIFF('2019-07-27', activity_date) > 0
GROUP BY activity_date

/*
def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('activity_date', as_index=False).agg(
        active_users = ('user_id','nunique')    
    )

    last_date = pd.to_datetime('2019-07-27')
    first_date = last_date - pd.DateOffset(days=29)

    df = df[df['activity_date'].isin(pd.date_range(first_date,last_date) )]
    df.columns = ['day','active_users']
    return df 
*/
