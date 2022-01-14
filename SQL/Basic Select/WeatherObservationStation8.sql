/*
 Author: Eda AYDIN
 Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
 */

SELECT DISTINCT CITY
FROM   STATION
WHERE  REGEXP_LIKE(CITY,'^[aeiouAEIOU].*[aeiouAEIOU]$');

/*
 Upperco
Aguanga
East China
East Irvine
Amo
Eleele
Oconee
Amazonia
Aliso Viejo
Andersonville
Arkadelphia
Eriline
Eastlake
Arispe
Ermine
Eufaula
Osborne
Elm Grove
Atlantic Mine
Oshtemo
Archie
Alpine
Ojai
Urbana
Alba
Eskridge
Ozona
Acme
 */