/*
 Author: Eda AYDIN

 Write a query calculating the amount of error and round it up to the next integer.
 Employees: ID, Name, SALARY
 */

SELECT CEIL(AVG(SALARY) - AVG(REPLACE(SALARY, "0","")))
FROM EMPLOYEES

/*
 2253
 */