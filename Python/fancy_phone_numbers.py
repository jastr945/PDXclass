'''Fancy phone numbers
Write a small app that asks the user for an all-digits phone number, Then 'pretty prints' it out.
Use the the `input()` builtin function.
'''


phone_number = str(input('Please enter the 10-digits phone number: '))

print('(' + phone_number[:3] + ') ' + phone_number[3:6] + '-' + phone_number[6:])