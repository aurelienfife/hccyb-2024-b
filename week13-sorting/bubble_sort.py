# Bubble sort

names = ["Mark", "Arthur", "Aurelien", "Jim", "Lorna", "Owen"]

# Flag for sorted list
sorted = False
# Main while loop
while not sorted:
    # Assume sorted
    sorted = True
    # Inspect the numbers
    for index in range(1, len(names)):
        # If wrong order, swap them
        if names[index] < names [index - 1]:
            # Swap them, Python way
            names[index], names[index-1] = names[index-1], names[index]

            # In other languages, swapping may require using a temporary variable

            # if swap happens, then it's not sorted
            sorted = False

print(names)
