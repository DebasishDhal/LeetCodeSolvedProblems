/*
Table: Employees
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table. This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them. Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer. Return the result table ordered by employee_id. The result format is in the following example.
*/

-- # Write your MySQL query statement below
SELECT
    emp1.employee_id,
    emp1.name,
    COUNT(emp2.employee_id) AS reports_count,
    ROUND(AVG(emp2.age),0) AS average_age
FROM Employees emp1
INNER JOIN Employees emp2 
ON emp1.employee_id = emp2.reports_to
GROUP BY emp1.employee_id
ORDER BY emp1.employee_id

/*
import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employees, 
                        left_on = 'reports_to', right_on = 'employee_id', #employees before .merge uses its reports_to and employees just after ( uses its employee_id key to join.
                        suffixes=('', '_report') #Many col names in both tables are the same. '',i.e. (original names) gets attached to left col names and _report gets attached to right col names
                        )

    df = df.groupby(['employee_id_report','name_report'], as_index=False).agg( #grouping by employee_id_report is enough, I'm putting name_report because we have to diplay manager name.
                        reports_count=('employee_id_report', 'count'),
                        average_age=('age', 'mean')
                    ).rename(
                        columns = {'employee_id_report':'employee_id', 'name_report':'name'}
                    )

    df['average_age'] = (df['average_age']+ 1e-12).round(0) #This is the pièce de résistance of the code. 1e-12 ensures that 0.5 gets rounded to 1 always.

    return df
*/
