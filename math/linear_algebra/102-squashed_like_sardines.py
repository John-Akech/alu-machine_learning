#!/usr/bin/env python3

def cat_matrices(mat1, mat2, axis=0):
    # Check if mat1 and mat2 are lists and not empty
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    # Helper function to check if two matrices can be concatenated along the specified axis
    def can_concatenate(m1, m2, axis):
        # Flatten matrices to check dimensions
        def flatten(m):
            result = []
            stack = [m]
            while stack:
                item = stack.pop()
                if isinstance(item[0], list):
                    stack.extend(item)
                else:
                    result.extend(item)
            return result
        
        flat1 = flatten(m1)
        flat2 = flatten(m2)
        
        # Convert matrices to numpy arrays to leverage shape comparison and concatenation
        import numpy as np
        np_m1 = np.array(flat1)
        np_m2 = np.array(flat2)
        
        # Check if concatenation along axis is possible
        try:
            np.concatenate((np_m1, np_m2), axis=axis)
            return True
        except ValueError:
            return False

    # Check if matrices can be concatenated
    if not can_concatenate(mat1, mat2, axis):
        return None
    
    # Convert lists to numpy arrays for concatenation
    import numpy as np
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)

    # Concatenate along the specified axis
    result = np.concatenate((np_mat1, np_mat2), axis=axis)
    
    # Convert back to list and return
    return result.tolist()
