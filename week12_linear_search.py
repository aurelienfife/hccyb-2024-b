'''
Linear Search

- an indexed collection (list, array etc...)
- a search term
- a flag whether found or not

Algorithm

For loop, length of collection
    If current element is equal to search term then
        set flag to found
        print current index
        break out of loop
    else
        continue
End of loop

If flag is "not found"
    Display "Not found"


'''

# Implementation in Python
found = False
# Set up list
things_mark_likes = ["Networking", "Coffee", "Dad Jokes", "Buying me coffee"]
# Get a search term
search_term = input("What do you want to search for?")

for index in range(len(things_mark_likes)):
    if search_term.lower() == things_mark_likes[index].lower():
        print("Found at index:", index)
        found = True
        break

if found == False:
    print("Not found")


second_list = []
for index in range(len(things_mark_likes)):
    thing = (index, things_mark_likes[index])
    second_list.append(thing)

print(second_list)