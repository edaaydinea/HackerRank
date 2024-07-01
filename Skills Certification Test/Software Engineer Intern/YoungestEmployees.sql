/*
Enter your query here.

There are two tables with employee information: EMPLOYEE and EMPLOYEE_UIN. Query the tables to generate a list of all employees who are less than 25 years old first in order of NAME, then of ID, both in ascending order. The result should include the UIN followed by the NAME. 

*/

SELECT EMPLOYEE_UIN.UIN, EMPLOYEE.NAME
FROM EMPLOYEE
JOIN EMPLOYEE_UIN
ON EMPLOYEE.ID = EMPLOYEE_UIN.ID
WHERE EMPLOYEE.AGE < 25
ORDER BY EMPLOYEE.NAME, EMPLOYEE.ID;
