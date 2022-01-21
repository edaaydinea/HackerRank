/*
 Problem: Write a query to print total number of unique hackers who made at least 1
 submission each day (starting on the first day of the contest),
 and find the hacker_id and name of the hacker who made maximum number of
 submissions each day. If more than one such hacker has a maximum number of
 submissions, print the lowest hacker_id. The query should print this information
 for each day of the contest, sorted by the date.
 */
 SELECT SUBMISSION_DATE,
        (SELECT COUNT(DISTINCT HACKER_ID)
            FROM SUBMISSIONS AS S2
            WHERE S1.SUBMISSION_DATE = S2.SUBMISSION_DATE
            AND ( SELECT COUNT(DISTINCT S3.SUBMISSION_DATE)
                FROM SUBMISSIONS AS S3
                WHERE S2.HACKER_ID = S3.HACKER_ID
                AND S1.SUBMISSION_DATE > S3.SUBMISSION_DATE)
                    = DATEDIFF(S1.SUBMISSION_DATE, "2016-03-01")),
        (SELECT HACKER_ID
            FROM SUBMISSIONS AS S2
            WHERE S1.SUBMISSION_DATE = S2.SUBMISSION_DATE
            GROUP BY HACKER_ID
            ORDER BY COUNT(SUBMISSION_ID) DESC, HACKER_ID
            LIMIT 1) AS TOP_HACKER_ID,
        (SELECT NAME
            FROM HACKERS
            WHERE HACKER_ID = TOP_HACKER_ID)
FROM (SELECT DISTINCT  SUBMISSION_DATE
        FROM SUBMISSIONS) AS S1
GROUP BY SUBMISSION_DATE
