/*
 Author: Eda AYDIN

 Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
 */

SELECT DISTINCT CITY
FROM   STATION
WHERE  NOT REGEXP_LIKE(CITY,'^.*[aeiouAEIOU]$');

/*
 Addison
Agency
Alanson
Albany
Albion
Algonac
Allerton
Alton
Andover
Anthony
Arlington
Arrowsmith
Athens
Auburn
Baker
Baldwin
Bass Harbor
Beaufort
Beaver Island
Benedict {-truncated-}
 */