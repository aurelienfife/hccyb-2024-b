# Enter the name of 5 students
# And their marks
# Display their grade (pass / fail)

# message -> parameter
def input_grade(message, lowerLimit=0, upperLimit=100):
    grade = int(input(message))
    while grade < lowerLimit or grade > upperLimit:
        print('It needs to be between', lowerLimit, '-', upperLimit)
        grade = int(input(message))
    return grade

# grade student
def grade_student(name, marks, passmark = 50):
    if marks > passmark:
        print(name, "- pass")
    else:
        print(name, " - fail")


def main():
    # Save students and grades to lists
    students = []
    grades = []

    # Enter number of students and do input n times
    studentNum = int(input("Enter the number of students"))
    for index in range(studentNum):
        name = input('Enter name for student' + str(index + 1))
        students.append(name)
        grade = input_grade('Enter grade for student' + str(index+1))
        grades.append(grade)

    for index in range(studentNum):
        grade_student(students[index], grades[index])

# Checks if script is loaded as program
# as opposed to module
# and run main program accordingly
if __name__ == "__main__":
    main()

