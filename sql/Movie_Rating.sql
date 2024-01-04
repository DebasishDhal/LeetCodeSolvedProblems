/* https://leetcode.com/problems/movie-rating
Table: Movies
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table. title is the name of the movie.
 
Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
 
Table: MovieRating
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table. This table contains the rating of a movie by a user in their review. created_at is the user's review date. 
 
Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name. 
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
*/

(SELECT u.name as results
    FROM MovieRating m
    INNER JOIN Users u ON m.user_id = u.user_id
    GROUP BY u.user_id
    ORDER BY COUNT(m.rating) DESC, u.name ASC
LIMIT 1
)

UNION ALL

(SELECT movies.title as results
    FROM Movies
    INNER JOIN MovieRating m ON Movies.movie_id = m.movie_id
    WHERE MONTH(m.created_at) = 2 AND YEAR(m.created_at) = 2020
    GROUP BY m.movie_id
    ORDER BY AVG(m.rating) DESC, movies.title ASC


/*
  import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:

    df1 = movie_rating.merge(users, on='user_id', how='inner')
    df1 = df1.groupby(by=['user_id','name'],as_index= False).agg(
        results = ('rating','count')
    )
    df1 = df1.sort_values(by = ['results','name'], ascending = [False, True])[['name']].iloc[:1].rename(
        columns = {'name':'results'}
    )
    
    movie_rating = movie_rating.query("'2020-02-01' <= created_at <= '2020-02-28'")
    # movie_rating = movie_rating[(movie_rating['created_at'].dt.year == 2021) & (movie_rating['created_at'].dt.month == 2)] #Another way
    df2 = movie_rating.merge(movies, on='movie_id',how='inner')
    df2 = df2.groupby(by = ['movie_id','title'],as_index=False).agg(
        results = ('rating','mean')
    )
    df2 = df2.sort_values(by= ['results','title'],ascending = [False, True])[['title']].iloc[:1].rename(
        columns = {'title':'results'}
    )

    return pd.concat([df1,df2])
*/
