"""
Write a program that prompts the user for a word.

Print out either  `snake_case` or `CamelCase` depending case convention it is!.

Use substring membership with the `in` operator.
"""

word = str(input('Enter a word: '))

if '_' in word:
    print('It\'s a snake case.')
elif word == word.capitalize() or ' ' not in word:
    print('It\'s a camel case.')
else:
    print('It\'s a normal case.')