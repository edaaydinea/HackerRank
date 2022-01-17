/*
 Author: Eda AYDIN

 Query the average population of all cities in CITY where District California
 */

SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = "CALIFORNIA"

/*
 113000.667
 */