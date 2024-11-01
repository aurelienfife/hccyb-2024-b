'''
We will work through this exercise in class and run it in debug so we can see what happens
Write a program which asks the user for two numbers, adds them together, then tells the user the answer. We have done similar before! But this time:
•	The user interaction (asking for the numbers and outputting the result) happens in the main function
•	The adding of the two numbers happens in a function called add
•	The Add function will take the two numbers as parameters and return the results
•	The Add function will be called in the Main code, and the result will be returned to the main code

'''

# def receives two numbers a & b and returns c (the sum)
def add(a, b):      # name and input parameters
    c = a + b       # data processing
    return c        # output

# main program
def main():
    num1 = int(input('Enter the first number'))
    num2 = int(input('Enter the second number'))
    result = add(num1, num2)
    print(result)

if __name__ == '__main__':
    main()
