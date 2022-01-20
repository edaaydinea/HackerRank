/*
 Write a query identifying the type of each record in the TRIANGLES table
 using its three side lengths.

 A = B : ISOSCELES
 A = B = C: EQULIATERAL TRIANGLE
 A != B != C : SCALENE TRIANGLE
 A + B < C : IT IS NOT TRIANGLE

 Author: Eda AYDIN
 */

SELECT CASE WHEN (A+B<=C OR A+C<=B OR B+C<=A) THEN "Not A TriangLe"
            WHEN (A=B AND B=C) THEN "Equilateral"
            WHEN (A=B OR B=C OR A=C) THEN "Isosceles"
            ELSE "Scalene"
    END
FROM TRIANGLES
