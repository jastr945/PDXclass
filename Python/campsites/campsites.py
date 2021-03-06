"""
'FIND A CAMPGROUND'

This program will allow users to search for a limited number of campgrounds in Oregon by a keyword
(for example, if a user enters "Rocky Bend", the program will display the profile of the Rocky Bend Campground).

Each campsite profile will contain basic information, such as location, number of spaces (capacity), facilities, ect.

Depending on the type of the campground, the user will get profiles with different categories.

If a campground name is missing in the database, the user can create a new record and insert it into the database.

* THINGS I LEARNED AND PRACTICED WHILE WRITING THIS CODE:
- working with Sqlite3, using SQL language in Python
- creating and manipulating a database
- requests package and API
- creating classes and class inheritance
- making classes inherit the database from the connection object
- creating an auto-increment field (ID number)
- using new built-in functions and methods (fetchall(), quit(), zip(), .description, commit(), execute())
- accessing a list of tuples by index
- using RegEx to extract the name of the city from the address string
- using Python decorators (@staticmethod)

"""


import sqlite3
import requests
import re


conn = sqlite3.connect('campgrounds.db')


class DatabaseManager(object):
    """
    A connection object that uses Sqlite3 package to create and manipulate SQLite database.
    """
    def syncdb(self):
        """
        Creates a database and deletes it if it already exists.
        """
        conn.execute('''DROP TABLE IF EXISTS CAMPGROUNDS''')  # preventing "sqlite3.OperationalError: table already exists"

        conn.execute('''CREATE TABLE CAMPGROUNDS  
                         (ID              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                         NAME             TEXT    NOT NULL,
                         TYPE             TEXT    NOT NULL,
                         LOCATION         TEXT    NOT NULL,
                         CAPACITY         INT     NOT NULL,
                         PARKING          TEXT    NOT NULL,
                         INTERNET         TEXT    NOT NULL,
                         RESTROOMS        TEXT    NOT NULL,
                         SHOWERS          TEXT    NOT NULL,
                         POOL             TEXT    NOT NULL,
                         PET_FRIENDLY     TEXT    NOT NULL,
                         FAMILY_FRIENDLY  TEXT    NOT NULL,
                         WATER_HOOK_UP    TEXT    NOT NULL,
                         SEWER_HOOK_UP    TEXT    NOT NULL,
                         PICNIC_AREA      TEXT    NOT NULL);''')  # creating the table and columns

        # populating the table:

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Rocky Bend Campground', 'Tent sites', 'Upper Nestucca River Rd, Beaver, OR 97108', 6, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'No')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Deerwood RV Park', 'RV park', '35059 Seavey Loop Rd, Eugene, OR 97405', 50, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'No', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Packard Creek Campground', 'Tent sites', 'NF-21, Westfir, OR 97492', 35, 'Yes', 'No', 'Vault toilet', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Mt Hood Village RV Resort', 'RV park', '65000 E. Hwy 26, Welches, OR 97067', 382, 'Yes', 'Yes', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Portland Fairview RV Park', 'RV park', '21401 NE Sandy Blvd, Fairview, OR 97024', 407, 'Yes', 'No', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'No playground', 'Yes', 'Yes', 'No')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Barton Park', 'Tent sites', '19009 SE Barton Park Rd, Boring, OR 97009', 112, 'Yes', 'No', 'Vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Dougan Creek Campground', 'Tent sites', 'Park Rd, Washougal, WA 98671', 7, 'Yes', 'No', 'Flush toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Jantzen Beach RV Park', 'RV park', '1503 N Hayden Island Dr, Portland, OR 97217', 85, 'Yes', 'Yes, high-speed', 'Flush toilets', 'Yes', 'Yes', 'Yes', 'Playground, clubhouse, game room, basketball court', 'Yes', 'Yes', 'No')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Lower Falls Campground', 'Tent sites', '42218 NE Yale Bridge Rd, Amboy, WA 98601', 43, 'Yes', 'No', 'Accessible vault toilets', 'No', 'No', 'Yes', 'No playground', 'No', 'No', 'Yes')");

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                      VALUES ('Promontory Park Campground', 'Tent sites', '40600 OR-224, Estacada, OR 97023', 46, 'Yes', 'No', 'Accessible restrooms', 'Yes', 'No', 'Yes', 'A fishing lake just for kids', 'No', 'No', 'Yes')");

        conn.commit()

    def get_all(self):
        """
        Returns the data from the table in a form of a dictionary.
        """
        cursor = conn.execute("SELECT * FROM CAMPGROUNDS")
        columns = [i[0] for i in cursor.description]            # .description method returns the names of all columns
        return [dict(zip(columns, i)) for i in cursor.fetchall()]  # .fetchall method fetches all rows of a query result set and returns a list of tuples. Zip function matches the two tuples into one. Dict makes a dictionary of of it.

    def get(self, id):
        """
        Returns a row from the table depending on ID (primary key).
        """
        cursor = conn.execute("SELECT * FROM CAMPGROUNDS WHERE ID={}".format(id))
        columns = [i[0] for i in cursor.description]            # .description method returns the names of all columns
        return [dict(zip(columns, i)) for i in cursor.fetchall()]  # .fetchall method fetches all rows of a query result set and returns a list of tuples. Zip function matches the two tuples into one. Dict makes a dictionary of of it.

    @staticmethod
    def get_location(id):
        """
        Returns the name of the city or village where the campround is located. Will be used in Weather class to download weather for specific location.
        """
        cursor = conn.execute("SELECT * FROM CAMPGROUNDS WHERE ID={}".format(id))
        columns = [i[0] for i in cursor.description]
        my_loc = [dict(zip(columns, i)) for i in cursor.fetchall()]
        address = [i['LOCATION'] for i in my_loc]
        city = re.split('[\s:/,.:]', str(address))
        return city[-4]

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

        new_data = (new_name, new_type, new_location, new_capacity, new_parking, new_internet, new_restrooms, new_showers, new_pool, new_pet_friendly, new_family_friendly, new_water_hook_up, new_sewer_hook_up, new_picnic_area)

        conn.execute("INSERT INTO CAMPGROUNDS (NAME,TYPE,LOCATION,CAPACITY,PARKING,INTERNET,RESTROOMS,SHOWERS,POOL,PET_FRIENDLY,FAMILY_FRIENDLY,WATER_HOOK_UP, SEWER_HOOK_UP,PICNIC_AREA) \
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", new_data,);

        conn.commit()

        print('Your record was successfully saved in the database.')

    def delete(self, id):
        """
        Deletes a row in the table according to its ID (primary key).
        """
        conn.execute("DELETE FROM CAMPGROUNDS WHERE ID={}".format(id))
        print('Record deleted successfully.')


class Weather(object):
    """
    Imports the current weather data from OpenWeatherMap website.
    """
    def __init__(self, id):
        self.id = id

    def get_weather(self):
        package = {
            'APPID': '6b919e5d511686a6a70d2728794a6fe5',
            'q': str(self.city)
        }

        r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)
        json_data = r.json()
        return '{}\nTemperature: {:.2f} F\nPressure: {} hpa\nHumidity: {} %\nWind speed: {} m/s'\
            .format(json_data['weather'][0]['description'], json_data['main']['temp'] * 9/5 - 459.67, json_data['main']['pressure'], json_data['main']['humidity'],json_data['wind']['speed'])


class Campground(DatabaseManager, Weather):
    """
    Contains a prototype of every campground and inherits functionality of the DatabaseManager class.
    """
    def __init__(self, id, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family):
        self.id = id
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
        self.city = DatabaseManager.get_location(self.id)

    def __repr__(self):
        return ('ID: {}\nCampground: {}\nType: {}\nLocation: {}\nCapacity: {}\nParking: {}\nInternet: {}\nToilet: {}\n '
                 'Showers: {}\nPool: {}\nPet-friendly: {}\nFamily-friendly: {}').format(
            self.id, self.name,self.camptype, self.location, self.capacity, self.parking, self.internet, self.restrooms,
            self.showers, self.pool, self.pets, self.family)


class RV(Campground):
    """
    Adds whether there is a sewer and water hook-up available in RV parks.
    """
    def __init__(self, id, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family, water, sewer):
        super().__init__(id, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family)
        self.water = water
        self.sewer = sewer

    def __repr__(self):
        return 'Campground: {}\nType: {}\nLocation: {}\nCapacity: {}\nParking: {}\nInternet: {}\nToilet: {}\nShowers: ' \
                   '{}\nPool: {}\nPet-friendly: {}\nFamily-friendly: {}\nWater hook-up: {}\nSewer hook-up: {}\nWeather: {}'.format(self.name, self.camptype, self.location, self.capacity, self.parking, self.internet, self.restrooms, self.showers, self.pool, self.pets, self.family, self.water, self.sewer, self.get_weather())


class Tentsite(Campground):
    """
    Adds whether there is a picnic area available on campsites.
    """
    def __init__(self, id, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family, picnic):
        super().__init__(id, name, camptype, location, capacity, parking, internet, restrooms, showers, pool, pets, family)
        self.picnic = picnic

    def __repr__(self):
        return 'Campground: {}\nType: {}\nLocation: {}\nCapacity: {}\nParking: {}\nInternet: {}\nToilet: {}\nShowers: '\
                   '{}\nPool: {}\nPet-friendly: {}\nFamily-friendly: {}\nPicnic area: {}\nWeather: {}'.format(self.name, self.camptype, self.location, self.capacity, self.parking, self.internet, self.restrooms, self.showers, self.pool, self.pets, self.family, self.picnic, self.get_weather())


mydb = DatabaseManager()
print('Welcome to the Oregon Campgrounds Database!')


def search():
    """
    Looks for the name enter by the user and returns the row containing the name.
    """
    mystr = str(input('Enter the name of a campground you want to find (for example, Mt Hood or Rocky Bend): ')).capitalize()

    cursor = conn.execute("SELECT * FROM CAMPGROUNDS WHERE NAME LIKE ?", ('%' + mystr + '%',))
    row_list = [i for i in cursor.fetchall()]  # .fetchall method fetches all rows of a query result set and returns a list of tuples.
    if not row_list:
        mystr = str(input('There is no such campground in our database. Would you like to add a new record?(Y/N) ')).upper()
        if mystr == 'Y':
            print(mydb.create())
            quit()
        else:
            print('The program will now close.')
            quit()

    type_column = row_list[0][2]
    if type_column == 'RV park':
        return RV(id=row_list[0][0], name=row_list[0][1], camptype=row_list[0][2], location=row_list[0][3], capacity=row_list[0][4], parking=row_list[0][5], internet=row_list[0][6], restrooms=row_list[0][7], showers=row_list[0][8], pool=row_list[0][9], pets=row_list[0][10], family=row_list[0][11], water=row_list[0][12], sewer=row_list[0][13])
    else:
        return Tentsite(id=row_list[0][0], name=row_list[0][1], camptype=row_list[0][2], location=row_list[0][3], capacity=row_list[0][4], parking=row_list[0][5], internet=row_list[0][6], restrooms=row_list[0][7], showers=row_list[0][8], pool=row_list[0][9], pets=row_list[0][10], family=row_list[0][11], picnic=row_list[0][14])


print(search())


