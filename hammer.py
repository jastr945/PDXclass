# Hammer Lab
# Write a function that returns the meal for any given hour of the day or night in respect to the following schedule:


# Breakfast: 7AM - 9AM
#
# Lunch: 12PM - 2PM
#
# Dinner: 7PM - 9PM
#
# Hammer: 10PM - 4AM



am_or_pm = str(input('AM or PM? ')).capitalize()
hour_of_day = int(input('Enter an hour (from 1 to 12): '))

def am_meal(hour):
    if hour in range(7,10):
        return "It's breakfast"
    elif hour in range(1,4) or hour == 12:
        return 'Hammer'
    else:
        return 'It\'s not the time to eat!'

def pm_meal(hour):
    if hour in range(1,2) or hour == 12:
        return 'It\'s lunch!'
    elif hour in range(7,9):
        return 'It\'s dinner'
    elif hour in range(10,12):
        return 'Hammer'
    else:
        return 'It\'s not the time to eat!'

if am_or_pm =='AM':
    print(am_meal(hour_of_day))
else:
    print(pm_meal(hour_of_day))

