"""
'FIND A CAMPGROUND'

This program will allow users to search for a limited number of the most famous campgrounds in Oregon by a keyword
(for example, if a user enters "Woodburn", the program will display the profile of the Woodburn RV Park).

Each campsite profile will contain basic information, such as location, number of spaces (capacity), facilities available, ect.

The program downloads weather data and displays the current weather for the area where each campsite is located.

If a campground name is missing in the database, the user is able to create a new record and insert it into the database.


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


class DatabaseManager(object):
    """
    A connection object that uses sqlite3 package to create and manipulate SQLite relational database.
    """
    def __init__(self, database):

        self.database = database

        self.conn = sqlite3.connect(database) # opening the database

        # self.conn.close() # closing the database; need to put somewhere.


    def syncdb(self):
        """
        Creates a database and deletes it if it already exists.
        """
        self.conn.execute('''DROP TABLE IF EXISTS CAMPGROUNDS''')  # preventing "sqlite3.OperationalError: table already exists"

        self.conn.execute('''CREATE TABLE CAMPGROUNDS  
                         (ID              INT PRIMARY KEY AUTOINCREMENT    NOT NULL,
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
                         PICNIC_AREA      TEXT    NOT NULL);''')  # creating the table and columns

        # populating the table:

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Rocky Bend Campground', 'Tent sites', 'Upper Nestucca River Rd, Beaver, OR 97108', 6, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'No')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Deerwood RV Park', 'RV park', '35059 Seavey Loop Rd, Eugene, OR 97405', 50, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'No', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Packard Creek Campground', 'Tent sites', 'NF-21, Westfir, OR 97492', 35, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Mt Hood Village RV Resort', 'RV park', '65000 E. Hwy 26, Welches, OR 97067', 382, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Portland Fairview RV Park', 'RV park', '21401 NE Sandy Blvd, Fairview, OR 97024', 407, 'Yes', 'No', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Barton Park', 'Tent sites', '19009 SE Barton Park Rd, Boring, OR 97009', 112, 'Yes', 'No', 'Vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Dougan Creek Campground', 'Tent sites', 'Washougal, WA 98671', 7, 'Yes', 'No', 'Flush toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Jantzen Beach RV Park', 'RV park', '1503 N Hayden Island Dr, Portland, OR 97217', 85, 'Yes', 'Yes, high-speed', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Playground, clubhouse, game room, basketball court', 'Yes', 'Yes', 'No')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Lower Falls Campground', 'Tent sites', '42218 NE Yale Bridge Rd, Amboy, WA 98601', 43, 'Yes', 'No', 'Accessible vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Promontory Park Campground', 'Tent sites', '40600 OR-224, Estacada, OR 97023', 46, 'Yes', 'No', 'Accessible restrooms', 'Yes', 'No', 'Yes', 'A fishing lake just for kids', 'No', 'No', 'Yes')");

        self.conn.commit()

    def get_all(self):
        """
        Returns the data from the table in a form of a dictionary.
        """
        cursor = self.conn.execute("SELECT * FROM CAMPGROUNDS")
        columns = [i[0] for i in cursor.description]            # .description method returns the names of all columns
        return [dict(zip(columns, i)) for i in cursor.fetchall()]  # .fetchall method fetches all rows of a query result set and returns a list of tuples. Zip function matches the two tuples into one. Dict makes a dictionary of of it.

    def get(self, id):
        """
        Returns a row from the table depending on ID (primary key).
        """
        cursor = self.conn.execute("SELECT * FROM CAMPGROUNDS WHERE ID={}".format(id))
        columns = [i[0] for i in cursor.description]            # .description method returns the names of all columns
        return [dict(zip(columns, i)) for i in cursor.fetchall()]  # .fetchall method fetches all rows of a query result set and returns a list of tuples. Zip function matches the two tuples into one. Dict makes a dictionary of of it.

    def search(self):
        """
        Looks for the name enter by the user and returns the row containing the name.
        """
        mystr = str(input('Enter the name of a campground you want to find: ')).capitalize()
        cursor = self.conn.execute("SELECT * FROM CAMPGROUNDS WHERE NAME LIKE ?", ('%'+mystr+'%',))
        columns = [i[0] for i in cursor.description]            # .description method returns the names of all columns
        return [dict(zip(columns, i)) for i in cursor.fetchall()]  # # .fetchall method fetches all rows of a query result set and returns a list of tuples. Zip function matches the two tuples into one. Dict makes a dictionary of of it.

    def create(self):
        """
        Inserts a new row into the table using the data entered by the user.
        """
        new_name = str(input("Enter the name of a campground: ")).capitalize()
        new_type = str(input("Enter the type(Tent sites or RV park): "))
        new_location = str(input("Enter the address: ")).capitalize()
        new_capacity = int(input("Enter the number of sites available: "))
        new_parking = str(input("Is there a parking(Yes / No)? ")).capitalize()
        new_internet = str(input("Is there a WiFi connection available? "))
        new_restrooms = str(input("Enter the type of restrooms: "))
        new_showers = str(input("Are there showers available? "))
        new_pool = str(input("Is there a pool(Yes / No)? ")).capitalize()
        new_pet_friendly = str(input("Is the place pet-friendly? ")).capitalize()
        new_family_friendly = str(input("Is the place family-friendly? List the facilities for kids: "))
        new_water_hook_up = str(input("Is there a water hook-up(Yes / No)? ")).capitalize()
        new_sewer_hook_up = str(input("Is there a sewer hook-up(Yes / No)? ")).capitalize()
        new_picnic_area = str(input("Is there a picnic area available(Yes / No) ?")).capitalize()

        new_data = (new_name,new_type,new_location,new_capacity,new_parking,new_internet,new_restrooms,new_showers,new_pool,new_pet_friendly,new_family_friendly,new_water_hook_up,new_sewer_hook_up,new_picnic_area)

        self.conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (new_data,));

        self.conn.commit()

        print('Your record was successfully saved in the database.')

    def delete(self, id):
        """
        Deletes a row in the table according to its ID (primary key).
        """
        self.conn.execute("DELETE FROM CAMPGROUNDS WHERE ID={}".format(id))
        print('Record deleted successfully.')


class Campground:
    """
    Contains a prototype of every campground and inherits functionality of the DatabaseManager class.
    """
    def __init__(self, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family):
        # super(DatabaseManager, self).__init__(":memory:")
        self.name = name
        self.camptype = camptype
        self.location = location
        self.capacity = capacity
        self.parking = parking
        self.internet = internet
        self.restrooms = restrooms
        self.showers = showers
        self.pool = pool
        self.pets = pets
        self.family = family

    def __repr__(self):
        return 'Campground: {}\nType: {}\nLocation: {}\nCapacity: {}\nParking: {}\nInternet: {}\nToilet: {}\nShowers: ' \
               '{}\nPool: {}\nPet-friendly: {}\nFamily-friendly: {}'.format(self.name,self.camptype,self.location,self.capacity,self.parking,self.internet,self.restrooms,self.showers,self.pool,self.pets,self.family)


class RV(Campground, DatabaseManager):
    """
    Adds whether there is a sewer and water hook-up available in RV parks.
    """
    def __init__(self, water, sewer):
        super(Campground, self).__init__()
        self.water = water
        self.sewer = sewer


class Tentsite(Campground, DatabaseManager):
    """
    Adds whether there is a picnic area available on campsites.
    """
    def __init__(self, name, picnic_area):
        super().__init__(name)
        self.picnic_area = picnic_area


# class Weather
# Works with APIs to dowload the current weather reports for each location.

mydb = DatabaseManager('campgrounds.db')
print('Welcome to the Oregon Campgrounds Database!')
print(Campground(name='blabla',camptype='Camp',location='portland',capacity=6,parking='yes',internet='yes',restrooms='yes',showers='yes',pool='no',pets='no',family='yes'))
#print(mydb.syncdb())
# print(mydb.create())
# print(mydb.get_all())


