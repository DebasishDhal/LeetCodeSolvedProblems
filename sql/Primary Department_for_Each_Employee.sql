/*
Table: Employee
+---------------+---------+
| Column Name   |  Type   |
+---------------+---------+
| employee_id   | int     |
| department_id | int     |
| primary_flag  | varchar |
+---------------+---------+
(employee_id, department_id) is the primary key (combination of columns with unique values) for this table. employee_id is the id of the employee. department_id is the id of the department to which the employee belongs. primary_flag is an ENUM (category) of type ('Y', 'N'). If the flag is 'Y', the department is the primary department for the employee. If the flag is 'N', the department is not the primary. Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.
*/

-- # Write your MySQL query statement below, main question is how to select those employees who are into only one department, thus their primary_flag is 'N'.
SELECT 
    employee_id, department_id
FROM 
    Employee
WHERE   
    primary_flag = 'Y' OR
    employee_id IN 
        (SELECT employee_id 
        FROM Employee
        GROUP BY employee_id
        HAVING COUNT(DISTINCT department_id) = 1
        )

/*
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['count'] = employee.groupby('employee_id').department_id.transform('count')
    employee = employee.query("primary_flag =='Y' | count == 1 ")
    return employee[['employee_id','department_id']]

*/
