# Example of conditional loop

correct_password = 'pass123'

password = input('Enter your password')

while password != correct_password:
    print('Your password is incorrect, try again!')
    password = input('Password: ')

print('Welcome')
