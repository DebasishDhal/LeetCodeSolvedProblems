/*
Table: Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values. This table has the information about all people waiting for a bus. The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table. Turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board. weight is the weight of the person in kilograms.
There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.
Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.
*/

-- # Write your MySQL query statement below. Beats 83% of users.
SELECT
    person_name
FROM (
    SELECT
        person_name,
        turn,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_sum
    FROM
        Queue -- You cannot apply WHERE cumulative_sum <= 1000 here because MySQL doesn't allow setting up an alias and using the same alias in one SELECT statement. 
) AS subquery
WHERE cumulative_sum <= 1000
ORDER BY turn DESC
LIMIT 1;

/*
import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # queue.sort_values(by=['turn'],inplace=True)
    # queue['cum_sum'] = queue['weight'].cumsum()
    # queue = queue.query('cum_sum <= 1000')
    # return pd.DataFrame(data = [queue.iloc[-1]['person_name']], columns = ['person_name'])
    
    queue.sort_values(by=['turn'],inplace=True)
    total = 0
    queue['cum_sum'] = queue['weight'].cumsum()

    for i in range(0,len(queue)):
        total = total + queue['weight'].iloc[i]
        if total > 1000:
            index = i-1
            break

    if i == len(queue)-1 and total <= 1000:
        index = i
        
    return pd.DataFrame({'person_name':[queue['person_name'].iloc[index]]})

*/
