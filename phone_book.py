# The following is just an example used in class. The actual code is below:

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


# PHONEBOOK LAB

phonebook = {'Katie': {'name': 'Katie', 'number': '2109415792', 'phrase': 'friend'},
            'Charlie': {'name': 'Charlie', 'number': '504699679', 'phrase': 'neighbor'},
            'Chelsea': {'name': 'Chelsea', 'number': '2109415778', 'phrase': 'sister'},
             'James': {'name': 'James', 'number': '5689412374', 'phrase': 'son'}}


running = True
while running:
    try:
        query = int(input('Enter 1 to create a contact, 2 to retrieve contact, 3 to update contact and 4 to delete contact: '))
    except ValueError:
        print('Imput must be a number. Please try again.')
        continue

    if query == 1:
        add_name = str(input('Enter a name: ')).capitalize()
        add_number = str(input('Enter a number: '))
        add_phrase = str(input('Enter a phrase: '))
        newdictionary = {'name': add_name, 'number': add_number, 'add_phrase': add_phrase}
        phonebook.update(newdictionary)
        print('Your new contact has been created successfully: ' + str(newdictionary.values()))

    elif query == 2:
        print('These are your options: ' + str(phonebook.keys()))
        name = (str(input('Which contact do you want to retrieve? '))).capitalize()
        if name in phonebook:
            print(phonebook[name])
        else:
            print('There is no such name. Try again.')

    elif query == 3:
        upd_name = str(input('What name would you like to update? ')).capitalize()
        del phonebook[upd_name]
        new_name = str(input('Enter a name: ')).capitalize()
        new_number = str(input('Enter a number: '))
        new_phrase = str(input('Enter a phrase: '))
        upd_dictionary = {'name': new_name, 'number': new_number, 'add_phrase': new_phrase}
        phonebook.update(upd_dictionary)
        print('Your contact has been updated successfully: ' + str(upd_dictionary.values()))

    elif query == 4:
        del_name = str(input('Which name would you like to delete?'))
        del phonebook[del_name]
        print(phonebook)
    else:
        print('Incorrect value. Please try again.')