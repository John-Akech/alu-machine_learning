#!/usr/bin/env python3

import numpy as np

def np_slice(matrix, axes={}):
    # Create a tuple with slices based on the provided axes
    slices = tuple(slice(None) if i not in axes else slice(*axes[i]) for i in range(matrix.ndim))
    return matrix[slices]
