/*
 Problem: https://www.hackerrank.com/challenges/occupations
 Author: Eda AYDIN
 */

SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT MIN(d), MIN(p), MIN(s), MIN(a)
FROM (SELECT CASE WHEN OCCUPATION = 'DOCTOR' THEN (@r1 := @r1 + 1)
                  WHEN OCCUPATION = 'PROFESSOR' THEN (@r2 := @r2 + 1)
                  WHEN OCCUPATION = 'SINGER' THEN (@r3 := @r3 + 1)
                  WHEN OCCUPATION = 'ACTOR' THEN (@r4 := @r4 + 1) END AS row_index,
             CASE WHEN OCCUPATION = 'DOCTOR' THEN NAME END AS d,
             CASE WHEN OCCUPATION = 'PROFESSOR' THEN NAME END AS p,
             CASE WHEN OCCUPATION = 'SINGER' THEN NAME END AS s,
             CASE WHEN OCCUPATION = 'ACTOR' THEN NAME END AS a
      FROM OCCUPATIONS
      ORDER BY NAME
     ) AS t
GROUP BY row_index