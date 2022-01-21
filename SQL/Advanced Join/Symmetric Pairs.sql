/*
 Problem:https://www.hackerrank.com/challenges/symmetric-pairs
 */
SELECT F1.X, F1.Y
FROM FUNCTIONS AS F1
JOIN FUNCTIONS AS F2 ON F1.X = F2.Y AND F1.Y = F2.X
GROUP  BY F1.X, F1.Y
HAVING COUNT(F1.X) >1 OR F1.X < F1.Y
ORDER BY F1.X