/*
 Problem:https://www.hackerrank.com/challenges/binary-search-tree-1
 */
 SELECT N, CASE WHEN P IS NULL THEN "Root"
                WHEN EXISTS(SELECT P
                    FROM BST
                    WHERE B.N = P
                    ) THEN "Inner"
                ELSE "Leaf"
            END
FROM BST AS B
ORDER BY N