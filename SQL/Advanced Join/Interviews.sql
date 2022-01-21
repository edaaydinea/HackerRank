/*
 Problems:https://www.hackerrank.com/challenges/interviews

 Contests: contest_id, hacker_id,name
 Colleges: college_id, contest_id
 Challenges: challenge_id,college_id
 View_Stats: challenge_id, total_views,total_unique_views
 Submission_Stats: challenge_id, total_submissions, total_accepted submissions


 Output: contest_id, hacker_id, name, sum_total_submissions,
 sum_total_accepted_submissions, sum_total_views, sum_total_unique_views
 */

SELECT C1.CONTEST_ID, C1.HACKER_ID, C1.NAME,
       SUM(SS.TOTAL_SUBMISSIONS) AS TOTAL_SUBMISSIONS_SUM,
       SUM(SS.TOTAL_ACCEPTED_SUBMISSIONS) AS TOTAL_ACCEPTED_SUBMISSIONS_SUM,
       SUM(VS.TOTAL_VIEWS) AS TOTAL_VIEWS_SUM,
       SUM(VS.TOTAL_UNIQUE_VIEWS) AS TOTAL_UNIQUE_VIEWS_SUM
FROM CONTESTS AS C1
JOIN COLLEGES AS C2 ON C1.CONTEST_ID = C2.CONTEST_ID
JOIN CHALLENGES AS C3 ON C2.COLLEGE_ID = C3.COLLEGE_ID
LEFT JOIN (SELECT CHALLENGE_ID,
                  SUM(TOTAL_VIEWS) AS TOTAL_VIEWS,
                  SUM(TOTAL_UNIQUE_VIEWS) AS TOTAL_UNIQUE_VIEWS
           FROM VIEW_STATS
           GROUP BY CHALLENGE_ID) AS VS
    ON C3.CHALLENGE_ID = VS.CHALLENGE_ID
LEFT JOIN (SELECT CHALLENGE_ID,
                  SUM(TOTAL_SUBMISSIONS) AS TOTAL_SUBMISSIONS,
                  SUM(TOTAL_ACCEPTED_SUBMISSIONS) AS TOTAL_ACCEPTED_SUBMISSIONS
           FROM SUBMISSION_STATS
           GROUP BY CHALLENGE_ID) AS SS
    ON C3.CHALLENGE_ID = SS.CHALLENGE_ID
GROUP  BY C1.CONTEST_ID, C1.HACKER_ID, C1.NAME
HAVING TOTAL_SUBMISSIONS_SUM != 0
    AND TOTAL_ACCEPTED_SUBMISSIONS_SUM != 0
    AND TOTAL_VIEWS_SUM != 0
    AND TOTAL_UNIQUE_VIEWS_SUM != 0
ORDER BY C1.CONTEST_ID

