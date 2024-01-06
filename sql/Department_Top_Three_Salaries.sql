/*
Simple, we have a employee table with their salary and rank. From there, we find the top three earners from each department.
Table: Employee
+--------------+---------+ 
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
Table: Department (This is a not the focus here, just a simple joining is all this table be used for)
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
+--------------+---------+
A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department. Write a solution to find the employees who are high earners in each of the departments. Return the result table in any order.
*/
-- # Write your MySQL query statement below

WITH ranked_employee AS (
    SELECT 
        *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank -- By partitioning over departmentId, we ask it to rank every row within its own group
    FROM Employee
) -- What this does is return a table called ranked_employee where each row is densly ranked within its own group. Dense rank is a form of rank where ranking numbers are not skipped in two or more rows have the rank rank.  If we want to just rank without any grouping, then DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank

SELECT d.name as Department, r.name as Employee, r.salary as Salary
FROM ranked_employee r INNER JOIN Department d ON r.departmentId = d.id
WHERE salary_rank <= 3 -- If we get 4 values who are second highest earner, then all 4 will have rank 2. The next smallest salary will have 3rd rank which also needs to be returned. 
 -- Hence dense rank

/*
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', 
                        how = 'inner', suffixes = ('_emp','_dept')) #Merging with unequal col names
    df['salary_rank'] = df.groupby('name_dept')['salary'].rank(method='dense',ascending=False) #Grouping and ranking

    df = df.query('salary_rank<=3')[['name_dept','name_emp','salary']]
    # df = df[df['salary_rank']<=3][['name_dept','name_emp','salary']]
    df.columns = ['Department','Employee','Salary']
    return df
*/
