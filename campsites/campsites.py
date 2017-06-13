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
Location: Woodburn, OR
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


class Searchable:
    """
    Contains a function allowing to search for a keyword. All other classes will inherit it.
    """
    def get_str(self):
        return '{}'.format(self.name)


class RV(Campground, Searchable):
    """
    Adds whether there is a sewer and water hook-up for RV's.
    """
    def __init__(self, name, water, sewer):
        super().__init__(name)
        self.water = water
        self.sewer = sewer


class Tentsite(Campground, Searchable):
    """
    Adds whether there is a picnic area on the campsite.
    """
    def __init__(self, name, picnic_area):
        super().__init__(name)
        self.picnic_area = picnic_area



