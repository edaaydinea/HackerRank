/*
 Problem: https://www.hackerrank.com/challenges/the-pads/
 Author: Eda AYDIN
 */
SELECT CONCAT(NAME, "(",SUBSTRING(OCCUPATION,1,1), ")")
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT("There are a total of ", COUNT(OCCUPATION), " ",LOWER(OCCUPATION),"s.") AS TOTAL
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY TOTAL