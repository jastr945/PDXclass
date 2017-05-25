# Simple version

# Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".**

# Check the solution using the doctest in the heading of the file and simply return whether the word follows the rule or not.

users_word = str(input('Enter a word: ')).lower()

def check_spelling(word):

    e_index = word.index('e')

    if word[e_index - 1] == 'i' and word[e_index - 2] == 'c':

        print('This word does not follow the rule')

    else:

        print('The word follows the rule.')

final_result = check_spelling(users_word)



# Advanced version

# Find a list of exceptions to use and check if the word given is an exception to the rule.

users_word = str(input('Enter a word: ')).lower()

exceptions = ['cheiromancies', 'cleidomancies', 'eigenfrequencies', 'obeisancies', 'oneiromancies', 'sufficient', 'efficient']

def check_spelling(word):

    e_index = word.index('e')

    if word in exceptions:

        print('This is an exception!')

        return

    if word[e_index - 1] == 'i' and word[e_index - 2] == 'c':

        print('This word does not follow the rule')

    else:

        print('The word follows the rule.')