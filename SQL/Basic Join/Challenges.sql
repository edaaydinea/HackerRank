/*
 Author: Eda AYDIN

 Write a query to print the hacker_id, name, and the total number of challenges created by each student.
 Sort your results by the total number of challenges in descending order.
 If more than one student created the same number of challenges, then sort the result by hacker_id.
 If more than one student created the same number of challenges and the count is less than the maximum
 number of challenges created, then exclude those students from the result.

 Hackers: hacker_id, name
 Challenges = challenge_id, hacker_id
 */
SELECT H.hacker_id, H.name, COUNT(C.challenge_id) AS c_count
FROM Hackers H
JOIN Challenges C ON C.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
HAVING c_count =(
    SELECT COUNT(C2.challenge_id) AS c_max
    FROM challenges as C2
    GROUP BY C2.hacker_id
    ORDER BY c_max DESC limit 1
    ) OR
  c_count IN (
    SELECT DISTINCT c_compare AS c_unique
    FROM (
        SELECT H2.hacker_id, H2.name, COUNT(challenge_id) AS c_compare
        FROM Hackers H2
        JOIN Challenges C ON C.hacker_id = H2.hacker_id
        GROUP BY H2.hacker_id, H2.name)
    counts
    GROUP BY c_compare
    HAVING COUNT(c_compare) = 1)
ORDER BY c_count DESC, H.hacker_id;
