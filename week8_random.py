import random

numbers = []
n = 0
for i in range(10000):
    num = random.randint(i + n, 5+n+i)
    n = num
    numbers.append(num)

#print(numbers)

search_term = numbers[9000]
# Linear search
counter = 0
for position in range(len(numbers)):
    counter += 1
    if numbers[position] == search_term:
        print("Number", search_term, " is found")
        print("Ran ", counter, "times")
        break


# Binary search
counter = 0
low = 0
high = len(numbers)
found = False

while found == False and low < high:
    counter += 1
    index = (low + high) // 2
    if numbers[index] == search_term:
        print("Found number", numbers[index])
        print("Ran", counter, "times")
        found = True
    elif search_term > numbers[index]:
        low = index
    else:
        high = index 
