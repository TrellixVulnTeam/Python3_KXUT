"""
Task 2
The valid phone number program.
Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.
"""
phone_number = input('Please, enter your phone number  ')
if phone_number.isdigit() and len(phone_number) == 10 and phone_number[0] == '0':
    print('Thank you for entering valid phone number!')
else:
    print('Please, enter right phone number')