from random import randrange

number_of_dice = int(input('What is the number of dice you want to roll? '))

number_of_sides = int(input('What is the number of sides? '))

for i in range(number_of_dice):

    print(randrange(1, number_of_sides))