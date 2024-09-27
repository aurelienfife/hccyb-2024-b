# Fixed loop: definite amount of iterations.

# Loop 50 times, display the first 50 numbers
# for index in range(50, 0, -1):
#     print(index)


#num = int(input('Enter a number between 1 and 10'))

for i in range(1,11):
    for j in range(1,11):
        print(str(i)+'x'+str(j),'=', i*j)


print('end')

# Lists - 

students = ['Jack', 'Conor', 'Ryan', 'Owen', 'Nathan']

for index in range(len(students)):
    print(index, '-',students[index].upper())
    students[index] = students[index][::-1]

print(students)