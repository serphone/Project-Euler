from math import sqrt
from functools import reduce
from operator import mul
from collections import Counter

from pyler import EulerProblem
from utils import prime_factors
from prime_generator import rwh_primes


class Problem0012(EulerProblem):
    """
    The sequence of triangle numbers is generated by adding the natural numbers.
    So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
    first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... Let us
    list the factors of the first seven triangle numbers:  1: 1 3: 1,3 6:
    1,2,3,610: 1,2,5,1015: 1,3,5,1521: 1,3,7,2128: 1,2,4,7,14,28 We can see that
    28 is the first triangle number to have over five divisors. What is the
    value of the first triangle number to have over five hundred divisors?
    """

    problem_id = 12
    simple_input = 5
    simple_output = 28
    real_input = 500
    real_output = 76576500

    @staticmethod
    def solver(input_val):
        n = 1
        t_n = 1  # n-th triangle number
        count = 0
        while count <= input_val:
            count = 0
            n += 1
            t_n += n
            for i in range(1, int(sqrt(t_n)) + 1):
                if t_n % i == 0:
                    count += 2
            if t_n == int(sqrt(t_n)) ** 2:  # for a perfect square
                count -= 1
        return t_n

    @staticmethod
    def solver2(input_val):
        def triangle_numbers(limit):
            """Generates triangle numbers."""
            triangle_number = 1
            for i in range(2, limit):
                yield triangle_number
                triangle_number += i

        primes = rwh_primes(10 ** 5)
        for number in triangle_numbers(10 ** 5):
            prime_factors_pow = []
            if number < 2:
                prime_factors_pow.append(0)
            for p in primes:
                if p > number:
                    break
                n = 0
                while number % p == 0:
                    n += 1
                    number //= p
                prime_factors_pow.append(n)
            num_divisors = 1
            for k in prime_factors_pow:
                num_divisors *= k + 1
            if num_divisors >= input_val:
                return number

    @staticmethod
    def solver3(input_val):
        n, nb_divisors = 1, 1

        while nb_divisors < input_val:
            n += 1
            factors = Counter(prime_factors(n * (n + 1) // 2))
            nb_divisors = reduce(mul, [x + 1 for x in factors.values()])

        return n * (n + 1) // 2


if __name__ == "__main__":
    import unittest

    unittest.main()