# Table: Employees

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the id and the name of an employee in a company.
 

# Table: EmployeeUNI

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | unique_id     | int     |
# +---------------+---------+
# (id, unique_id) is the primary key (combination of columns with unique values) for this table.
# Each row of this table contains the id and the corresponding unique id of an employee in the company.
 

# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

# Return the result table in any order.
#Beats 17% of users in runtime, but for once I don't care. I learnt how to merge using pandas, although its more convinient in SQL.

import pandas as pd
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees  =  employees.merge(employee_uni, on = 'id', how = 'left') #employee_uni is the right table here
    print(employees.columns)
    return employees[['unique_id','name']]
