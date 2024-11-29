'''
Binary search:
- list must be in order

pseudocode
low = 0
high = length of list

Set found flag to False

Repeat until found is true or low > high
    index = low + high / 2 (middle of list)

    If the element at the index is what look for
        set flag to true
        return index
    Else if the element is greater
        Set high boundary to index
    Else (element is lower)
        Set low boundary to index
End loop

'''

