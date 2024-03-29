/*
 Problem: https://www.hackerrank.com/challenges/placements
 */
SELECT S.NAME
FROM STUDENTS AS S
INNER JOIN PACKAGES AS P1 ON S.ID = P1.ID
INNER JOIN FRIENDS AS F ON S.ID = F.ID
INNER JOIN PACKAGES AS P2 ON F.FRIEND_ID = P2.ID
WHERE P2.SALARY > P1.SALARY
ORDER BY P2.SALARY