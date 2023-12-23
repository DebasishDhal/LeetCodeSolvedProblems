- Checking if content col has more than 15 chars: - ```df[df['content'].str.len()>15]```, this function is more efficient than ```df[df['content'].apply(len)>15]```, likely because apply method doesn't take advantage of vectorization.

- To merge two tables based on more than one condition in pandas, either use mergeasof or use .loc after using merge.
  
  - ```df = prices.merge(units_sold,on='product_id',how='left').loc[lambda x: (x.purchase_date.between(x.start_date,x.end_date))|(x.purchase_date.isnull())]``` : - Merge prices and units_sold table on ```product_id``` and then select only those columns where the purchase date is either non existent or lies between the start and end date. This is less efficient than the mergeasof method. ```soldWithPrices = pd.merge_asof(units_sold, prices, by='product_id', left_on='purchase_date', right_on='start_date')```. This one merges based on ```product_id``` and only selects those columns where ```start_date``` <= ```purchase_date```. 
