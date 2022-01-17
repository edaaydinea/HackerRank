/*
 Author: Eda AYDIN

 Query the sum of the populations for all Japanese cities in City. The COUNTRYCODE for Japan is JPN.
 */

SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = "JPN"

/*
 879196
 */