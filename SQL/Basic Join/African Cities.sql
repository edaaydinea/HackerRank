/*
 Author: Eda AYDIN
 */
SELECT CITY.NAME
FROM COUNTRY, CITY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE AND COUNTRY.CONTINENT = "AFRICA";

/*
 Qina
Warraq al-Arab
Kempton Park
Alberton
Klerksdorp
Uitenhage
Brakpan
Libreville
 */