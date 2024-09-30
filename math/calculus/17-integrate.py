#!/usr/bin/env python3

def poly_integral(poly, C=0):
    # Check if poly is a list of numbers and C is an integer
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None

    # Check if all elements in poly are integers or floats
    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    # Start with the constant of integration C
    integral = [C]

    # Loop through the polynomial and calculate the integral
    for i, coeff in enumerate(poly):
        if coeff == 0:
            integral.append(0)  # Append 0 for zero coefficients
        else:
            integral_value = coeff / (i + 1)  # Integral of x^i is (x^(i+1))/(i+1)
            if integral_value.is_integer():
                integral.append(int(integral_value))  # Convert to int if it's a whole number
            else:
                integral.append(integral_value)

    # Remove trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral

