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

"""

class Facilities:
    def __init__(self):


class Campground:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity