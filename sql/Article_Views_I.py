# Table: Views

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.
 

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

# The result format is in the following example.
#Beats 75% of users
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views
    df.sort_values(by=['author_id'], inplace=True)
    df = df.rename(columns = {'author_id':'id'})
    res = df[(df['viewer_id']==df['id'])].drop_duplicates(subset=['id'])
    return res[['id']]
