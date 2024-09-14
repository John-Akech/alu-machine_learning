#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]

# Extract the first two numbers
arr1 = arr[:2]

# Extract the last five numbers
arr2 = arr[-5:]

# Extract the 2nd through 6th numbers
arr3 = arr[1:6]

print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
