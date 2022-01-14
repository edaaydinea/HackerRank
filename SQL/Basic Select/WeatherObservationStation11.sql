/*
 Author: Eda AYDIN

 Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
 */

SELECT DISTINCT CITY
FROM   STATION
WHERE  NOT REGEXP_LIKE(CITY,'^[aeiouAEIOU].*[aeiouAEIOU]$');

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
Baileyville
Bainbridge
Baker
Baldwin
Barrigada
Bass Harbor {-truncated-}
 */