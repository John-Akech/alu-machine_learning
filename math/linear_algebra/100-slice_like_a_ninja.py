#!/usr/bin/env python3
""" Implements the np_slice method
"""
import numpy as np

def np_slice(matrix, axes={}):
    """ Slices a matrix along specified axes and limits
    """
    result = matrix
    
    for axis, slice_params in axes.items():
        # Extract the slice params
        start, end, step = extract_slice_params(slice_params)
        
        # Generate slice object
        slice_obj = slice(start, end, step)
        
        # Apply slicing along the specified axis
        result = np.take(result, np.arange(result.shape[axis])[slice_obj], axis=axis)
    
    return result

def extract_slice_params(slice_tuple):
    start = end = step = None

    # If only one value has been provided, it is the end value
    if len(slice_tuple) == 1:
        end = slice_tuple[0] or -1

    # If two values have been provided, then they are the start and end values
    elif len(slice_tuple) == 2:
        start, end = slice_tuple[0] or 0, slice_tuple[1] or -1

    # If three values have been provided, then they are the start, end and step values
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple[0] or 0, slice_tuple[1] or -1, slice_tuple[2] or 1
    
    return start, end, step
