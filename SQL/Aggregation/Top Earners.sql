/*
 Author: Eda AYDIN

  Write a query to find the maximum total earnings for all employees as well as the
 total number of employees who have maximum total earnings.
 Then print these values as 2 space-separated integers.

 Employee: employee_id, name, months, salary
 */

SELECT SALARY * MONTHS AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY EARNINGS
ORDER BY EARNINGS DESC
LIMIT 1

/*
 108064 7
 */