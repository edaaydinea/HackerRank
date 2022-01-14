/*
Author: Eda AYDIN
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
 */

SELECT DISTINCT CITY
FROM   STATION
WHERE  REGEXP_LIKE(CITY,'^.*[aeiouAEIOU]$');

/*
 Glencoe
Chelsea
Pelahatchie
Dorrance
Cahone
Upperco
Waipahu
Millville
Aguanga
Morenci
South El Monte
Gustine
Delano
Westphalia
Saint Elmo
Raymondville
Barrigada
Hesperia
Wickliffe
Milledgeville
East China
Gretna
Zionsville
Rio Oso
Samantha
Bentonville
Grosse Pointe
Robertsdale
Dale
Tennessee
Chokio
Bertha
Regina
Mascotte
Netawaka
East Irvine
Amo
Delta
Jerome
Baton Rouge
Clarkdale
Pheba
Eleele
Oconee
Grandville
Susanville
Rosie
Verona
De Tour Village
West Grove
Bono
Biggsville
Amazonia
Marysville
Cape Girardeau
Crane Lake
Grayslake
Bellevue
Lynnville
Hope
Aliso Viejo
Gowrie
Andersonville
Crouseville
Arkadelphia
Eriline
Howard Lake
Hagatna
Eastlake
Corriganville
Tarzana
Grapevine
Kanorado
Curdsville
Notasulga
Pleasant Grove
Skanee
Springerville
Yellow Pine
Ravenna
Brownsdale
Hayesville
Greenville
Yellville
Weldona
Cascade
Bayville
Arispe
Baileyville
Lakeville
Pico Rivera
Pawnee
Bainbridge
Dupo
Montrose
Ermine
Casco
Madisonville
Lismore
Eufaula
Wildie
Mosca
Lottie
Daleville
Cuba
Renville
Kirksville
Lydia
Monona
Lakota
Grand Terrace
Fort Meade
Hayneville
Losantville
Caseville
Pomona
Hopkinsville
Dixie
Hillside
Osborne
Elm Grove
Atlantic Mine
Honolulu
Oshtemo
Monroe
Archie
Alpine
Ojai
Urbana
Palatka
Yuma
Alba
Waresboro
Magnolia
Dundee
Chilhowee
Eskridge
Ozona
Woodsboro
Clio
Yalaha
Leakesville
Shasta
Calpine
Tina
Middleboro
Lena
Lee
Mid Florida
Acme
 */