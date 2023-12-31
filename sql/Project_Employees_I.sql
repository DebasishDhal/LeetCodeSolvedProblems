/*
able: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
 

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.
 

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.

The query result format is in the following example.
*/

-- # Write your MySQL query statement below. Beats 59%
SELECT
p.project_id,
# ROUND(AVG(e.experience_years),2) as average_years -- For some reason, sum/count is faster than avg method.
ROUND( (SUM(e.experience_years)/COUNT(e.experience_years)) , 2) as average_years
FROM Project p
INNER JOIN
Employee e
ON 
p.employee_id = e.employee_id
GROUP BY p.project_id

/* Beats 84%
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, how = 'inner', on = 'employee_id')

    df = df.groupby('project_id')['experience_years'].mean() \ #We group it by project_id. We want to take mean of experience only.
        .reset_index() \ #Grouping results in a Series. reset_index converts it into dataframe, with same col name as its parent col name
        .rename(columns = {'experience_years':'average_years'}) \ #Col name is renamed
        .round(2)

    return df*/
