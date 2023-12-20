/*
Table: Students

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
student_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one student in the school.
 

Table: Subjects

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
subject_name is the primary key (column with unique values) for this table.
Each row of this table contains the name of one subject in the school.
 

Table: Examinations

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
There is no primary key (column with unique values) for this table. It may contain duplicates.
Each student from the Students table takes every course from the Subjects table.
Each row of this table indicates that a student with ID student_id attended the exam of subject_name.
 

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.
*/

-- My solution. Pretty straightforward but takes time. For some reason, specifying ASC while ordering improves the performance. 
SELECT 
    students.student_id, 
    students.student_name, 
    subjects.subject_name, 
    COUNT(exam.subject_name) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations exam ON subjects.subject_name = exam.subject_name AND students.student_id = exam.student_id 
GROUP BY students.student_id, subjects.subject_name
ORDER BY students.student_id, subjects.subject_name;

-- The code below is the best solution. Uses cross join.
-- Write your MySQL query statement below
SELECT s.student_id, s.student_name, sj.subject_name, count(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sj --This is because we need all combinations of students and subjects. If a student hasn't taken a subject, it'd appear as 0.
LEFT JOIN Examinations e
ON s.student_id = e.student_id and sj.subject_name = e.subject_name
GROUP BY s.student_id,s.student_name, sj.subject_name
ORDER BY s.student_id, sj.subject_name;


-- Pandas solution
/*
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_count = examinations.groupby(['student_id','subject_name'])\
                            .size()\
                            .reset_index(name = 'attended_exams') #Size counts unique value of each ['student_id','subject_name'] unique tuple. Basically how many times a student appeared for a subject

    student_cross = students.merge(subjects, how = 'cross' ) #Cross because we also want to include subjects for which the student didn't appear. Otherwise we'd have used inner join

    combined = student_cross.merge(exam_count, how = 'left', on = ['student_id','subject_name']) #We want to retain a ['student_id','subject_name'] row even if it's non-existent. Since all possible ['student_id','subject_name'] tuples exist in student_cross, this will be our base table
    combined = combined.sort_values(by = ['student_id','subject_name'])

    combined['attended_exams'] = combined['attended_exams'].fillna(0) #If a student didn't appear for a subject, it should be 0
    return combined[['student_id','student_name','subject_name','attended_exams']]
*/
