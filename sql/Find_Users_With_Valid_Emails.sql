/*
Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
| mail          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table. This table contains information of the users signed up in a website. Some e-mails are invalid.
Write a solution to find the users who have valid emails. A valid e-mail has a prefix name and a domain where:
The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
The domain is '@leetcode.com'.
*/

# Write your MySQL query statement below. Beats 96%
SELECT 
    user_id, name, mail
FROM 
    Users
WHERE
    mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com' -- ^[a-zA-Z] takes care of the first char, [a-zA-Z0-9_.-]* takes care of everything before @, @leetcode[.]com does the obvious.

-- The [.] is required, otherwise . just means any characters.

/* Beats 37% users only due to many operations being involved. 
import pandas as pd
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users['prefix'] = users['mail'].apply(lambda x: x.split('@')[0])
    users['domain'] = users['mail'].apply(lambda x: x[x.find('@'):]) #Notice that I'm not using x.split('@)[1] for obvious reasons
    users = users[users['prefix'].apply(lambda x: re.match(r'^[a-zA-Z]', x) != None)] #First prefix character letter done
    users = users[users['prefix'].apply(lambda x: re.match(r'^[a-zA-Z0-9_.-]+$', x) != None)] #Prefix contain only a-zA-Z0-9._-
    users = users[users['domain']== '@leetcode.com'] #Domain = @leetcode.com done

    return users[['user_id','name','mail']]
#An elegant solution is this
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')]
    return df
