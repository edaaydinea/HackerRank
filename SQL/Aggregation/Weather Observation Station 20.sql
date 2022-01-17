/*
 Author: Eda AYDIN
 */

SET @index := -1;
SELECT ROUND(AVG(S2.LAT_N), 4)
FROM (
     SELECT @index := @index + 1 AS INDEX_, S.LAT_N
     FROM STATION AS S
     ORDER BY S.LAT_N
         ) AS S2
WHERE S2.INDEX_ IN (FLOOR(@index / 2), CEIL(@index / 2))

/*
 83.8913
 */