/*
Table: RequestAccepted
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 Write a solution to find the people who have the most friends and the most friends number. The test cases are generated so that only one person has the most friends.
*/

-- Crux of the problem is that if id = 1's friend request gets accepted by id = 2, 1 is friend of 2 and 2 is friend of 1. But since it is 1 who sent the request, in the table we'll only have 1(requester_id)->2(accepter_id)
-- That's why we need to have the original table, in union with requester_id and accepter_id columns interchanged.
(SELECT
    r1.requester_id, r2.accepter_id
FROM 
    RequestAccepted r1 CROSS JOIN RequestAccepted r2
WHERE 
    (r1.requester_id, r2.accepter_id) IN 
    (SELECT requester_id, accepter_id FROM RequestAccepted))

UNION

(SELECT
    r1.requester_id, r2.accepter_id
FROM 
    RequestAccepted r1 CROSS JOIN RequestAccepted r2
WHERE 
    (r1.accepter_id, r2.requester_id) IN 
    (SELECT requester_id, accepter_id FROM RequestAccepted))
/*
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    reverse = request_accepted.copy()
    # reverse['requester_id'] = request_accepted['accepter_id']
    # reverse['accepter_id'] = request_accepted['requester_id']
    reverse = reverse.rename(columns = {'requester_id':'accepter_id','accepter_id':'requester_id'})

    df = pd.concat( [request_accepted,reverse], axis = 0 )
    # df.drop_duplicates(subset=['requester_id','accepter_id'],inplace=True)

    df = df.groupby('requester_id',as_index=False).agg(
        num = ('accepter_id','nunique')
    ).rename(
        columns={'requester_id':'id'}
    ).sort_values(
        by='num',
        ascending = False
    ).iloc[:1]

    # print(df.shape)
    return df
*/
