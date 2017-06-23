my_change = int(input('What is the amount of change? '))

def quaters_calculation(change):

    quaters = change // 25

    return quaters, change - quaters * 25

def dimes_calculation(change):

    dimes = change // 10

    return dimes, change - dimes * 10

def nickels_calculation(change):

    nickels = change // 5

    return nickels, change - nickels * 5

def pennies_calculation(change):

    pennies = change

    return pennies, change - pennies

while my_change > 0:

    quaters, my_change = quaters_calculation(my_change)

    dimes, my_change = dimes_calculation(my_change)

    nickels, my_change = nickels_calculation(my_change)

    pennies, my_change = pennies_calculation(my_change)

    print('Your change is {} quaters, {} dimes, {} nickels and {} pennies'. format(quaters,dimes,nickels,pennies))