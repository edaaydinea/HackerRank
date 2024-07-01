/*
Enter your query below.
Please append a semicolon ";" at the end of the query

The data for the number employed at several famous IT companies is maintained in the COMPANY table.
Write a query to print the IDs of the companies that have more than 10000 employees, in ascending order of ID.
*/

SELECT ID
FROM COMPANY
WHERE EMPLOYEES > 10000
ORDER BY ID ASC;