# running = True
# while running:
#
#     try:
#         query = input('Enter 1 to search phonebook, enter 2 to quit: ')
#     except ValueError:
#         print('Imput must be a number. Please try again.')
#         continue
#
#     if query == '1':
#         print('Thank you.')
#     elif query == '2':
#         quit()
#     else:
#         print('I did not understand that')


# Phonebook Lab

phonebook = {'Katie': {'name': 'Katie', 'number': '2109415792', 'phrase': 'friend'},
            'Charlie': {'name': 'Charlie', 'number': '504699679', 'phrase': 'neighbor'},
            'Chelsea': {'name': 'Chelsea', 'number': '2109415778', 'phrase': 'sister'},
             'James': {'name': 'James', 'number': '5689412374', 'phrase': 'son'}}

running = True
while running:
    try:
        query = int(input('Enter 1 to add a contact, 2 to retrieve contact, 3 to update contact and 4 to delete contact: '))
    except ValueError:
        print('Imput must be a number. Please try again.')
        continue

    if query == 1:
        pass
    if query == 2:
        print(phonebook.keys())
        name = (str(input('Which contact do you want to retrieve? '))).capitalize()
        if name == 'Katie':
            print(phonebook['Katie'])
        elif name == 'Charlie':
            print(phonebook['Charlie'])
        elif name == 'Chelsea':
            print(phonebook['Chelsea'])
        elif name == 'James':
            print(phonebook['James'])
        else:
            print('There is no such name. Please try again.')



