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


class DatabaseManager:
    """
    A connection object that uses sqlite3 package to create and manipulate SQLite relational database.
    """

    conn = sqlite3.connect('campgrounds.db') # opening the database

    conn.execute('''DROP TABLE IF EXISTS CAMPGROUNDS''')

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



    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (1, 'Rocky Bend Campground', 'Tent sites', 'Upper Nestucca River Rd, Beaver, OR 97108', 6, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (2, 'Deerwood RV Park', 'RV park', '35059 Seavey Loop Rd, Eugene, OR 97405', 50, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'No', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (3, 'Packard Creek Campground', 'Tent sites', 'NF-21, Westfir, OR 97492', 35, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (4, 'Mt Hood Village RV Resort', 'RV park', '65000 E. Hwy 26, Welches, OR 97067', 382, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (5, 'Portland Fairview RV Park', 'RV park', '21401 NE Sandy Blvd, Fairview, OR 97024', 407, 'Yes', 'No', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (6, 'Barton Park', 'Tent sites', '19009 SE Barton Park Rd, Boring, OR 97009', 112, 'Yes', 'No', 'Vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (7, 'Dougan Creek Campground', 'Tent sites', 'Washougal, WA 98671', 7, 'Yes', 'No', 'Flush toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (8, 'Jantzen Beach RV Park', 'RV park', '1503 N Hayden Island Dr, Portland, OR 97217', 85, 'Yes', 'Yes, high-speed', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Playground, clubhouse, game room, basketball court', 'Yes', 'Yes', 'No')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (9, 'Lower Falls Campground', 'Tent sites', '42218 NE Yale Bridge Rd, Amboy, WA 98601', 43, 'Yes', 'No', 'Accessible vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

    conn.execute("INSERT INTO CAMPGROUNDS (ID,NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,TOILET,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
          VALUES (10, 'Promontory Park Campground', 'Tent sites', '40600 OR-224, Estacada, OR 97023', 46, 'Yes', 'No', 'Accessible restrooms', 'Yes', 'No', 'Yes', 'A fishing lake just for kids', 'No', 'No', 'Yes')");

    conn.commit()


    cursor = conn.execute("SELECT * FROM CAMPGROUNDS")
    for row in cursor:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Type:", row[2])
        print("Location:", row[3])
        print("Capacity:", row[4])
        print("Parking:", row[5])
        print("Internet:", row[6])
        print("Toilet:", row[7])
        print("Showers:", row[8])
        print("Pool:", row[9])
        print("Pet friendly:", row[10])
        print("Family / kids friendly:", row[11])
        print("Water hook-up:", row[12])
        print("Sewer hook-up:", row[13])
        print("Picnic area:", row[14], '\n')

    conn.close()

    id = None

    def syncdb(self):
        """
        Creates a database and deletes it if it already exists.
        """
        pass

    def delete(id):
        """
        Deletes a row in the table according to its ID (primary key).
        """
        cursor.execute('''DELETE FROM CAMPGROUNDS WHERE ID=id''')
        print('Record deleted successfully.')

    # @staticmethod
    def get(id):
        """
        Selects a row from the table according to ID (primary key) and displays it.
        """
        cursor = conn.execute('''SELECT * FROM CAMPGROUNDS WHERE ID=id''')
        for row in cursor:
            print("ID:", row[0])
            print("NAME:", row[1])
            print("TYPE:", row[2])
            print("LOCATION:", row[3])
            print("CAPACITY:", row[4])
            print("PARKING:", row[5])
            print("INTERNET:", row[6])
            print("TOILET:", row[7])
            print("SHOWERS:", row[8])
            print("POOL:", row[9])
            print("PET_FRIENDLY:", row[10])
            print("FAMILY_FRIENDLY:", row[11])
            print("WATER_HOOK_UP:", row[12])
            print("SEWER_HOOK_UP:", row[13])
            print("PICNIC_AREA:", row[14], '\n')

    # @staticmethod
    def search(search_str):  # wyszukaj w bazie
        pass

    def update(self): # logika, ktora bedzie zapisywac do bazy danych wszystkie atrybuty
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


class RV(Campground, DatabaseManager):
    """
    Adds whether there is a sewer and water hook-up available in RV parks.
    """
    def __init__(self, name, water, sewer):
        super().__init__(name)
        self.water = water
        self.sewer = sewer


class Tentsite(Campground, DatabaseManager):
    """
    Adds whether there is a picnic area available on campsites.
    """
    def __init__(self, name, picnic_area):
        super().__init__(name)
        self.picnic_area = picnic_area



