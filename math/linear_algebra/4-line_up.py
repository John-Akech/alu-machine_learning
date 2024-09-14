#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    # Check if both arrays have the same length
    if len(arr1) != len(arr2):
        return None
    # Return a new list with element-wise sums of the arrays
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

# Test cases
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))  # Output: [6, 8, 10, 12]
    print(arr1)  # Output: [1, 2, 3, 4]
    print(arr2)  # Output: [5, 6, 7, 8]
    print(add_arrays(arr1, [1, 2, 3]))  # Output: None
