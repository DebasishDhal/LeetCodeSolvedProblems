/*
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.
*/

--  Write your MySQL query statement below
-- We join the Weather table with itself based on a condition.
-- Beats 52% of users.
SELECT 
weather.id AS 'id'
FROM 
weather
JOIN 
weather w 
ON 
DATEDIFF(weather.recordDate,w.recordDate) = 1
WHERE 
weather.Temperature > w.Temperature


/*
#Beats 95% 
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True) 
    weather['dateShifted'] = weather['recordDate'].shift(1) #We shift the days back by 1. if recordDate - 12 oct 2023, dateShifted = 11 oct 2023
    weather['temperatureShifted'] = weather['temperature'].shift(1) #Similarly we have shift the temperature one index back
    df = weather[( (pd.to_datetime(weather['recordDate']) - pd.to_datetime(weather['dateShifted'])).dt.days == 1) & (weather['temperature']>weather['temperatureShifted'])]
#We want rows where recordDate-dateShifted =1 (yesterday) (remember that type of weather['dateShifted') is str and needs to be converted into datetime format and today's date > #yesterdays' date
    return df[['id']]
*/
