/*
 Author: Eda AYDIN

 Write a query to print the hacker_id, name, and total score of the hackers ordered
 by the descending score.
 If more than one hacker achieved the same total score, then sort the result by ascending hacker_id.
 Exclude all hackers with a total score of 0 from your result.

 Hackers: hacker_id, name
 Submissions: submission_id, hacker_id, challenge_id, score
 */
SELECT H.hacker_id, H.name, SUM(Sscore)
FROM Hackers H
INNER JOIN (
    SELECT S.hacker_id, MAX(score) AS Sscore
    FROM Submissions S
    GROUP BY S.hacker_id, S.challenge_id)
S2 ON H.hacker_id = S2.hacker_id
GROUP BY H.hacker_id, H.name
HAVING SUM(Sscore) > 0
ORDER BY SUM(Sscore) DESC, H.hacker_id ASC;