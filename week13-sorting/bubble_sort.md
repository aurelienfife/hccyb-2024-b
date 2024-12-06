# Bubble Sort

The bubble sort algorithm looks at all the elements in an array/a list from left to right; compares them and swaps them accordingly.
The process repeats until no swaps occur, which indicates that the list has been sorted.

```
Bubble sort:

L: a list, not sorted
Sorted: a boolean, flagging if a swap occured (if so, not sorted)

Set sorted to false
Repeat while sorted is false

   Set sorted to true
   For loop, index from 1 to length of L

      If element of L at index is lower than element at index - 1 then
          Swap elements
          Set sorted to false
      End if

   Next index

Next repeat
```