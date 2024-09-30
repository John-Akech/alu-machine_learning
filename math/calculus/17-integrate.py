#!/usr/bin/env python3

"""Module for polynomial integration.

This module contains a function to compute the integral of a polynomial
represented by a list of coefficients.
"""

def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial.
        C (int, float): The integration constant (default is 0).

    Returns:
        list: A list of coefficients representing the integral of the
              polynomial, or None if the input is invalid.
    """
    # Check if poly is a list and C is an integer or float
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
        integral_value = coeff / (i + 1)  # Integral of x^i
        if integral_value.is_integer():
            integral.append(int(integral_value))  # Convert to int if whole number
        else:
            integral.append(integral_value)

    # Remove trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral


if __name__ == "__main__":
    # Example test cases
    print(poly_integral([5, 3, 0, 1]))  # Expected: [0, 5, 1.5, 0, 0.25]
    print(poly_integral([]))  # Expected: [0]
    print(poly_integral([1, 2, 3]))  # Expected: [0, 1, 1.0, 0.5]
    print(poly_integral([0, 0, 0]))  # Expected: [0]
    print(poly_integral("not a list"))  # Expected: None
    print(poly_integral([1, 2, "not a number"]))  # Expected: None

