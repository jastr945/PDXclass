# Palindrome Lab

word = str(input('Enter a word: '))

if word == word[::-1]:
    print('It\'s a palindrome!')
else:
    print('It\'s not a palindrome')