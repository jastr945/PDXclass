"""
'FIND A CAMPGROUND'

This program will allow users to search for a limited number of the most famous campgrounds in Oregon, depending on
keywords (for example, if a user types in "Woodburn", the program will display the profile of the Woodburn RV Park).
The program will take care of invalid user input, too. Each campsite profile will contain basic information, such as
location, number of spaces (capacity), facilities, ect. The program will download weather data and display the current weather
for the area where each campsite is located.


* If a profile is missing, the user can create it! (add this feature if I have time)

The profile will contain the list of facilities / amenities:
* Free Parking
* Free High Speed Internet ( WiFi )
* flush toilets / pit toilets
* showers
* pool
* pets allowed / pets not allowed (true/ false kind of choice)
* kid / family friendly (true / false kind of choice)
* for RV: water and sewer hook-ups.
* for tents: picnic areas


Example Output:

Campground: Woodburn RV Park
Type: RV Park
Location: Woodburn,OR
Capacity: 150
Parking: Yes
Internet: No Wi-Fi
Toilet: Flush toilets
Showers: Yes
Pool: No
Pet-friendly: Pets are allowed.
Family-friendly: Playground is available.
Water hook-up: Yes
Sewer hook-up: Yes

"""

import sqlite3


class Data:
    """
    A connection object that represents the database.
    """


    conn = sqlite3.connect('campgrounds.db')

    print("Opened database successfully")

    conn.execute('''CREATE TABLE CAMPGROUNDS
             (ID              INT PRIMARY KEY    NOT NULL,
             NAME             TEXT    NOT NULL,
             TYPE             TEXT    NOT NULL,
             LOCATION         TEXT    NOT NULL,
             CAPACITY         INT     NOT NULL,
             PARKING          TEXT    NOT NULL,
             INTERNET         TEXT    NOT NULL,
             TOILET           TEXT    NOT NULL,
             SHOWERS          TEXT    NOT NULL,
             POOL             TEXT    NOT NULL,
             PET_FRIENDLY     TEXT    NOT NULL,
             FAMILY_FRIENDLY  TEXT    NOT NULL,
             WATER_HOOK_UP    TEXT    NOT NULL,
             SEWER_HOOK_UP    TEXT    NOT NULL,
             PICNIC_AREA      TEXT    NOT NULL);''')

    print("Table created successfully")

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (1, 'Rocky Bend Campground', 'Campground', 'Upper Nestucca River Rd, Beaver, OR 97108', 6, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (2, 'Deerwood RV Park', 'RV park', '35059 Seavey Loop Rd, Eugene, OR 97405', 50, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'No', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (3, 'Packard Creek Campground', 'Campground', 'NF-21, Westfir, OR 97492', 35, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (4, 'Mt Hood Village RV Resort', 'RV park', '65000 E. Hwy 26, Welches, OR 97067', 382, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes')");

    conn.commit()

    print("Records created successfully")


    id = None

    def delete(self):  # usun mnie z bazy danych
        pass

    # @staticmethod
    def get(id):  # pobierz z bazy danych
        pass

    # @staticmethod
    def search(search_str):  # wyszukaj w bazie
        pass

    def save(self): # logika, ktora bedzie zapisywac do bazy danych wszystkie atrybuty
        pass

    def syncdb(self): # tworzy baze danych i przygotowuje tabele jesli tabela nie istnieje
        pass

class Campground:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity


class Facilities:
    def __init__(self, has_parking, has_internet, toilet, has_showers, has_pool, pet_friendly, family_friendly):
        self.has_parking = has_parking
        self.has_internet = has_internet
        self.toilet = toilet
        self.has_showers = has_showers
        self.has_pool = has_pool
        self.pet_friendly = pet_friendly
        self.family_friendly = family_friendly


# class Searchable:
#     """
#     Contains a function allowing to search for a keyword. All other classes will inherit it.
#     """
#     def get_str(self):
#         return '{}'.format(self.name)


class RV(Campground, Data):
    """
    Adds whether there is a sewer and water hook-up for RV's.
    """
    def __init__(self, name, water, sewer):
        super().__init__(name)
        self.water = water
        self.sewer = sewer


class Tentsite(Campground, Data):
    """
    Adds whether there is a picnic area on the campsite.
    """
    def __init__(self, name, picnic_area):
        super().__init__(name)
        self.picnic_area = picnic_area



