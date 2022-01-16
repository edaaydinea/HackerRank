/*
 Author: Eda AYDIN
 */
SELECT H.HACKER_ID, H.NAME
FROM   SUBMISSIONS S
JOIN CHALLENGES C ON S.CHALLENGE_ID = C.CHALLENGE_ID
JOIN difficulty D ON C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL
JOIN hackers H ON S.HACKER_ID = H.HACKER_ID AND S.SCORE = D.SCORE
GROUP  BY H.HACKER_ID, H.NAME
HAVING Count(S.HACKER_ID) > 1
ORDER  BY Count(S.HACKER_ID) DESC,  S.HACKER_ID ASC;

/*
 27232 Phillip
28614 Willie
15719 Christina
43892 Roy
14246 David
14372 Michelle
18330 Lawrence
26133 Jacqueline
26253 John
30128 Brandon
35583 Norma
13944 Victor
17295 Elizabeth
19076 Matthew
26895 Evelyn
32172 Jonathan
41293 Robin
45386 Christina
45785 Jesse
49652 Christine
13391 Robin
14366 Donna
14777 Gerald
16259 Brandon
17762 Joseph
28275 Debra
36228 Nancy
37704 Keith
40226 Anna
49307 Brian
12539 Paul
14363 Joyce
14658 Stephanie
19448 Jesse
20504 John
20534 Martha
22196 Anthony
23678 Kimberly
28299 David
30721 Ann
32254 Dorothy
46205 Joyce
47641 Patricia
13122 James
13762 Gloria
14863 Walter
18690 Marilyn
18983 Lori
21212 Timothy
25732 Antonio
28250 Evelyn
30755 Emily
38852 Benjamin
42052 Andrew
44188 Diana
48984 Gregory
13380 Kelly
13523 Ralph
21463 Christine
24663 Louise
26243 Diana
26289 Dorothy
39277 Charles
23278 Paula
25184 Martin
32121 Dorothy
36322 Andrew
39782 Tammy
40257 James
41319 Jean
10857 Kevin
25238 Paul
34242 Marilyn
39771 Alan
49789 Lillian
57947 Justin
74413 Harry
 */