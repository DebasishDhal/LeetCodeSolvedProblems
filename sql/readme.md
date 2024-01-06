- Checking if content col has more than 15 chars: - ```df[df['content'].str.len()>15]```, this function is more efficient than ```df[df['content'].apply(len)>15]```, likely because apply method doesn't take advantage of vectorization.

- To merge two tables based on more than one condition in pandas, either use mergeasof or use .loc after using merge.
  
  - ```df = prices.merge(units_sold,on='product_id',how='left').loc[lambda x: (x.purchase_date.between(x.start_date,x.end_date))|(x.purchase_date.isnull())]``` : - Merge prices and units_sold table on ```product_id``` and then select only those columns where the purchase date is either non existent or lies between the start and end date. This is less efficient than the mergeasof method. ```soldWithPrices = pd.merge_asof(units_sold, prices, by='product_id', left_on='purchase_date', right_on='start_date')```. This one merges based on ```product_id``` and only selects those columns where ```start_date``` <= ```purchase_date```. 

- Try to avoid ```COUNT(*)```. Instead use ```COUNT(DISTINCT(column_name))```, ```COUNT(column_name)``` or whatever seems suitable. This is to improve the speed of execution.

- You cannot have gap after ```COUNT``` just for the sake of aesthetics. ```COUNT(DISTINCT player_id)``` is right, while ```COUNT (DISTINCT player_id```) is wrong.

- ```
  df = df1.merge(df2, left_on = 'df1_table_col', right_on = 'right_table_col',
  suffixes = ('_df1cols','_df2cols'))
  ```
  This does a join beftween ```df1``` and ```df2``` using ```df1_table_col``` of df1 and ```df2_table_col``` of df2. The left and right suffix inside suffixes gets appended to columns of df1 and df2 respectively.
  
- If you need 38.5 to rounded to 39 always, use this trick. ```df['col'] = (df['col'] + 1e-12).round(0)```. A simple ```round(0)```, rounds it to 38.

- ```SELECT * ``` is way faster than ```SELECT col1,col2,col_last```. Also, better use ```IF(condition, 'True_Case', 'False_Case')``` instead of ```CASE WHEN condition THEN 'True_Case' ELSE 'False_Case' END```

- As a good practice, always use brackets when using ```UNION``` in SQL.
  
  ```
  (SELECT that AS result FROM this_table)
  UNION
  (SELECT this AS result FROM that_table)
  ```

- For producing a rank based on some column, with or without grouping, use this method: -
  - ```df['salary_rank'] = df.groupby('name_dept')['salary'].rank(method='dense',ascending=False)``` #salary_rank is rank of each row within its own group (grouped by name_dept). You can remove the groupby ranking is needed on entire table. The dense method doesn't skip ranks when it comes across same row values for col = 'salary'.
  - In SQL, it's done by Ranking and Partitioning.
    ```
    SELECT 
        *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
    ```
    To rank the whole table without any grouping,
    ```
    SELECT 
        *, 
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM Employee
    ```
- To use a temporary table created by you, use WITH method
  ```
  WITH my_table_alias AS (
      SELECT 
        *, 
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
  )

  SELECT * FROM my_table_alias
  ```
