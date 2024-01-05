/*
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. Each row of this table contains an email. The emails will not contain uppercase letters.
Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id. For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
*/

-- # Write your MySQL query statement below
DELETE p1
FROM person p1
INNER JOIN person p2 ON p1.email = p2.email AND p1.id > p2.id;

-- OR

DELETE
FROM person
WHERE Id NOT IN
(
  SELECT minid
  FROM
    (SELECT email, min(id) as minid
      FROM Person
      GROUP BY email 
    ) 
test)
