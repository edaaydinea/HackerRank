/*
Enter your query below.
Please append a semicolon ";" at the end of the query

Link: https://www.hackerrank.com/test/gfs8eiej4rq/questions/el2559on3gf

The times that employees log in and out are recorded over the course of a month. For each employee, determine the number of hours worked during the weekends.
For simplicity, hours worked in a day, hours are truncated to the their integer part.

For example, there are 10 hours between '2000-01-01 00:00:00' and '2000-01-01 10:00:00'. There are 9 hours between '2000-01-01 00:00:00' and '2000-01-01 09:59:59'.

Return a list of employee ids and weekend hours worked, descending by hours worked.

table name: attendance
columns: timestamp, emp_id
timestamp: varchar(20) date and time at which the employee logged in or logged out
emp_id: integer unique id of the employee

Example: 
Input
timestamp, emp_id
'2020-01-01 08:00:00', 747
'2020-01-01 17:00:00', 747
'2020-01-02 08:00:00', 747

Output
747 67
*/


SELECT emp_id, 
       SUM(FLOOR(hours_worked)) AS weekend_hours_worked
FROM (
    SELECT emp_id, 
           TIMESTAMPDIFF(HOUR, MIN(STR_TO_DATE(timestamp, '%Y-%m-%d %H:%i:%s')), MAX(STR_TO_DATE(timestamp, '%Y-%m-%d %H:%i:%s'))) AS hours_worked
    FROM attendance
    WHERE DAYOFWEEK(STR_TO_DATE(timestamp, '%Y-%m-%d %H:%i:%s')) IN (1, 7)
    GROUP BY emp_id, DATE(STR_TO_DATE(timestamp, '%Y-%m-%d %H:%i:%s'))
) AS t
GROUP BY emp_id
ORDER BY weekend_hours_worked DESC;


