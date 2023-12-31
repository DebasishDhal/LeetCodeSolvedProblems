/*
Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table. Each row of this table indicates the name and the ID of a student. id is a continuous increment. Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped. Return the result table ordered by id in ascending order.
*/

SELECT 
    CASE 
    WHEN id%2 = 0 THEN id-1
    WHEN id = (SELECT COUNT(*) FROM Seat) THEN id
    ELSE id+1 END AS id,
    student
FROM Seat
ORDER BY id

/*
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    studentList = seat['student']

    for i in range(int(len(studentList)/2)):
        studentList[2*i], studentList[2*i+1] = studentList[2*i+1], studentList[2*i]
    
    seat['student'] = studentList

    return seat
*/
