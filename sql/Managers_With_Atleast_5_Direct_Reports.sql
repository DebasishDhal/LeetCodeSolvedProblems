/*
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.
*/

SELECT E1.name 
FROM Employee E1
JOIN Employee E2
ON E1.id = E2.managerId
GROUP BY E1.id
HAVING count(E2.managerId) >= 5; --Where won't work after grouping


/*
import pandas as pd
#My solution. Beats 42%. 
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # employee.dropna(subset=['managerId'],inplace=True) #This was the problem. Just because a manager himself doesn't have a manager (i.e. managerId = null), he shouldn't be dropped

    df = employee.groupby(['managerId']).size().reset_index(name='count') 
    id_list = df[df['count']>=5]['managerId']
    res = employee[employee['id'].isin(id_list)]
    return res[['name']]

#Elegant solution of another person
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(
        'managerId', as_index=False
    ).agg(
        reporting=('id', 'count'),
    ).query(
        '5 <= reporting'
    )['managerId']

    return employee[
        employee['id'].isin(managers)
    ][['name']]
*.
