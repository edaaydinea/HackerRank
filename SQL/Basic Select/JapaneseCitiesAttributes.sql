/*
Author: Eda AYDIN

Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
*/

SELECT *
FROM CITY
WHERE COUNTRYCODE = "JPN"

/*
1613 Neyagawa JPN Osaka 257315 
1630 Ageo JPN Saitama 209442 
1661 Sayama JPN Saitama 162472 
1681 Omuta JPN Fukuoka 142889 
1739 Tokuyama JPN Yamaguchi 107078 
*/