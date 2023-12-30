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
