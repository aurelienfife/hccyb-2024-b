# Conditional loops
# Repeat code until a condition changes
# (or more likely, while nothing's changed)

# 1. set the correct answer
password = 'javascript'

# 2. 
guess = input('The password is the name of a programming language')

attempt = 0

# check validity of password and repeat if needed
while guess != password:
    attempt += 1
    if attempt == 3:
        print('Password attempts exceeded')
        exit()

    print('The input is invalid')
    guess = input('Try again')

print('Welcome!')
