'''
Input validation:
needing -> input
need to know -> 'validity criteria'   (age between 0 and 50)

get input
while input isn't valid:   (age < 0 or age > 50)
    get input again
'''

def main():
    print('This is only for people between 0 and 50')

    # First input
    age = int(input('How old are you?'))

    # Input validation stage
    # Will lock the program here until correct input
    while age < 0 or age > 50: # While input not valid
        print('Input invalid')
        print('This is only for people between 0 and 50')
        age = int(input('How old are you?'))

    # something
    print('hello world')


if __name__ == '__main__':
    main()

