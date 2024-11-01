'''
We will work through this exercise in class and run it in debug so we can see what happens
Write a program which creates a list of random numbers then outputs the list of random numbers. We have done something similar before! But this time:
•	The main code will welcome the user and tell them what will happen
•	We will write a function called create_list to create the list of random numbers
•	This function will take no parameters, and will return the list it has created
•	This function will be called by the Main code, and after it has completed, the Main code will have the new list and can print out the numbers in it
Let's try it together
'''

import random  # Import the random module for generating random numbers

# Function to create a list of 10 random integers between 1 and 100
def create_list():
    new_list = []
    for index in range(10):  # Loop 10 times
        new_list.append(random.randint(1, 100))  # Add a random integer to the list
    return new_list

# Main function to generate and print the random list
def main():
    l = create_list()  # Generate the list
    print(l)           # Print the list

# Execute main only if script is run directly
if __name__ == '__main__':
    main()
