/*
 Author: Eda AYDIN

 Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
 */

SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;

/*
 Aguanga
Alba
Albany
Amo
Andersonville
Archie
Athens
Atlantic Mine
Bainbridge
Baker
Bass Harbor
Bayville
Beaufort
Bellevue
Benedict
Bennington
Bentonville
Biggsville
Bison
Bono {-truncated-}
 */