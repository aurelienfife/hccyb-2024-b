
# I want to grade an assessment

marks = int(input('What are the assessment marks? 0 - 100'))

# Validate input - if not in the 0 - 100 bracket, prompt again

while marks < 0 or marks > 100:
    print(marks, 'is out of bounds.')
    marks = int(input('What are the assessment marks? 0 - 100'))

if marks >= 70:
    print('Grade A')
elif marks >= 60:
    print('Grade B')
elif marks >= 50:
    print('Grade C')
else:
    print('Fail')


