#!/usr/bin/env python3
"""Initializing the Poisson distribution"""


class Poisson:
    """Poisson class for poisson distribution"""

    e = 2.7182818285
    π = 3.1415926536

    def __init__(self, data=None, lambtha=1.):
        """Class constructor

        data: is a list of the data to be used to estimate the distribution
        lambtha: is the expected number of occurences in a given time frame
        """
        if data is None:
            self.lambtha = float(lambtha)
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """calculating the value of the PMF for a given number of
        successes

        k: is the number of successes

        Returns: the PMF value for k"""
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        f_k = 1
        for i in range(1, k + 1):
            f_k *= i
        return (self.e ** -self.lambtha) * (self.lambtha ** k) / f_k

    def cdf(self, k):
        """Calculating the value of the CDF for a given number of
        successes

        k: number of successes

        Return: CDF value for k"""
        if k < 0:
            return 0
        k = int(k)
        fx = 0
        for i in range(k + 1):
            fx += self.pmf(i)
        return fx
