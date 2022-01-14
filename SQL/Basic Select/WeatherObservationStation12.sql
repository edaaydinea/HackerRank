/*
 Author: Eda AYDIN
 Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
 */
SELECT DISTINCT CITY
FROM   STATION
WHERE  NOT REGEXP_LIKE(CITY,'^[aeiouAEIOU]') AND NOT REGEXP_LIKE(CITY,'^.*[aeiouAEIOU]$');

/*
 Baker
Baldwin
Bass Harbor
Beaufort
Beaver Island
Benedict
Bennington
Berryton
Beverly
Bison
Blue River
Bowdon
Bowdon Junction
Bridgeport
Bridgton
Brighton
Brilliant
Bristol
Brownstown
Buffalo Creek {-truncated-}
 */

