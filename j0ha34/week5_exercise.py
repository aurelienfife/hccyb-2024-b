
thesenumbers = [1,7,9,4,2,9,12,13,17]


# 1. You start from zero (keep track)
# 2. I scan the numbers from left to right
# 3. I add the number to temporary sum
# 4. Move on to next number

# 1.
total = 0

# 2.
for index in range(len(thesenumbers)):
    # print(index)
    # 3.
    total = total + thesenumbers[index]

print('Total:', total)

average_num = total / len(thesenumbers)
print('Average value: ', round(average_num, 2))
