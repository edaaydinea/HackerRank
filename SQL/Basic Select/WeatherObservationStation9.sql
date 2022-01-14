/*
 Author: Eda AYDIN
 Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
 */

SELECT DISTINCT CITY
FROM   STATION
WHERE  NOT REGEXP_LIKE(CITY,'^[aeiouAEIOU]');

/*
 Kissee Mills
Loma Mar
Sandy Hook
Tipton
Turner
Slidell
Negreet
Glencoe
Chelsea
Chignik Lagoon
Pelahatchie
Hanna City
Dorrance
Monument
Manchester
Prescott
Graettinger
Cahone
Sturgis
Highwood
Waipahu
Bowdon
Tyler
Watkins
Republic
Millville
Bowdon Junction
Morenci
South El Monte
Hoskinston
Talbert
Mccomb
Kirk
Carlock
Seward
Gustine
Delano
Westphalia
Saint Elmo
Roy
Pattonsburg
Centertown
Norvell
Raymondville
Beaver Island
Jemison
West Hills
Barrigada
Hesperia
Wickliffe
Culdesac
Roselawn
Forest Lakes
San Simeon
Little Rock
Portland
New Century
Hampden
Pine City
Sandborn
Seaton
Milledgeville
Prince Frederick
Pomona Park
Gretna
Yazoo City
Zionsville
Rio Oso
Jolon
Childs
Shreveport
Forest
Sizerock
Buffalo Creek
Winsted
Woodbury
Samantha
Hackleburg
Soldier
Columbus
Bentonville
Kirkland
Grosse Pointe
Wilton
Busby
Robertsdale
Dale
Reeds
Hayfork
Mcbrides
Lee Center
Tennessee
Henderson
Palm Desert
Benedict
Tamms
Haubstadt
Chokio
Clancy
Scotts Valley
Norwood
Bertha
Bridgeport
Cherry
Regina
Griffin
Pine Bluff
Mascotte
Baldwin
Netawaka
Pony
Franklin
Vulcan
Prairie Du Rocher
Delta
Carver
Paron
Winchester
Jerome
Baton Rouge
Greenview
Lucerne Valley
Cromwell
Quinter
Whitewater
Round Pond
Clarkdale
Rockton
Pheba
North Berwick
Grandville
Susanville
Rosie
Verona
Richland
Fremont
Philipsburg
Kensett
De Tour Village
Koleen
Winslow
Reasnor
West Grove
Frankfort Heights
Bono
Biggsville
Linthicum Heights
Marysville
Cape Girardeau
Pengilly
Newton Center
Crane Lake
Newbury
Kismet
Canton
Clipper Mills
Grayslake
Pierre Part
Bison
Bellevue
Ridgway
South Britain
Rydal
Lynnville
Deerfield
Montreal
Hope
Gowrie
Knob Lick
Crouseville
Cranks
Rives Junction
Ledyard
Norway
Rantoul
Richmond Hill
Fredericktown
Glen Carbon
Fredericksburg
Mc Henry
Wellington
Hoffman Estates
Howard Lake
Ducor
Salem
Sturdivant
Hagatna
Larkspur
Patriot
Corriganville
Carlos
Tarzana
Grapevine
Kanorado
Climax
Curdsville
Southport
Compton
Notasulga
Rumsey
Rogers
Pleasant Grove
Skanee
Springerville
Libertytown
Church Creek
Yellow Pine
Dumont
Gales Ferry
Ravenna
Williams
Decatur
Holbrook
Sherrill
Brownsdale
Linden
Sedgwick
Fort Atkinson
Peachtree City
Rocheport
West Somerset
Clovis
Heyburn
Peabody
Marion Junction
Randall
Hayesville
Jordan
White Horse Beach
Greenville
Macy
Flowood
Deep River
Napoleon
Leavenworth
Coldwater
Weldon
Yellville
Turners Falls
Delray Beach
Mineral Point
Weldona
Midpines
Cascade
Tefft
Showell
Bayville
Brighton
Grimes
Nubieber
North Monmouth
Harmony
Beaufort
Humeston
Baileyville
Lakeville
Firebrick
Pico Rivera
Ludington
Channing
West Baden Springs
Pawnee
Melber
Bainbridge
Sanders
Dupo
Montrose
Schleswig
Harbor Springs
Richmond
Siler
Reeves
Clifton
Casco
Crescent City
Madisonville
Lismore
Panther Burn
Hanscom Afb
Wildie
Mosca
Bennington
Lottie
Garland
Clutier
Lupton
Northfield
Daleville
Cuba
Norris
Clopton
Renville
Saint Paul
Kirksville
Kingsland
Fairview
Lydia
Bridgton
Brownstown
Monona
Hartland
Lakota
Grand Terrace
Mesick
Dryden
Beverly
Marine On Saint Croix
Pocahontas
Fort Meade
Hayneville
Yoder
Gatewood
Madden
Losantville
Cheswold
Caseville
Pomona
Hopkinsville
Jack
Dixie
Hillside
Hawarden
Cannonsburg
North Branford
New Liberty
Woodstock Valley
Farmington
Honolulu
Pfeifer
Gridley
Fulton
Winter Park
Monroe
Del Mar
Greens Fork
Garden City
Blue River
New Ross
Brilliant
Norphlet
Mechanic Falls
North Middletown
Keyes
Neon
Calhoun
Mullan
Coalgood
Walnut
Saint Petersburg
Julian
Veedersburg
Payson
Windom
Ludlow
Lindsay
Palatka
Bristol
Yuma
Zachary
Waresboro
Hills
Montgomery City
Delavan
Magnolia
Byron
Dundee
Baker
Hyde Park
Groveoak
Kenner
Many
Berryton
Chilhowee
Newark
Cowgill
Novinger
Goodman
Cobalt
South Haven
West Hyannisport
Jackson
Lapeer
Peaks Island
Hazlehurst
Chester
Clarkston
Healdsburg
Hotchkiss
Ravenden Springs
Kell
Strasburg
Five Points
Norris City
Coaling
Corcoran
Greenway
Woodsboro
Strawn
Dent
Shingletown
Clio
Yalaha
Leakesville
Fort Lupton
Shasta
South Carrollton
Taft
Calpine
Knobel
Bullhead City
Tina
Haverhill
Middleboro
Siloam
Lena
Lee
Freeport
Mid Florida
Gorham
Bass Harbor
Granger
 */