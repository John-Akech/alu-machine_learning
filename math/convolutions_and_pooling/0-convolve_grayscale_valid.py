#!/usr/bin/env python3

import numpy as np

def convolve_grayscale_valid(images, kernel):
    # Get the dimensions of images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape
    
    # Calculate the dimensions of the output after valid convolution
    output_h = h - kh + 1
    output_w = w - kw + 1
    
    # Initialize the output array with zeros
    output = np.zeros((m, output_h, output_w))
    
    # Perform convolution on each image
    for i in range(m):  # Loop over each image
        for x in range(output_h):  # Loop over the output height
            for y in range(output_w):  # Loop over the output width
                # Extract the current region of the image and apply the kernel
                region = images[i, x:x+kh, y:y+kw]
                output[i, x, y] = np.sum(region * kernel)
    
    return output
