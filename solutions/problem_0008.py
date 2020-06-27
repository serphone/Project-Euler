from functools import reduce
from operator import mul

from pyler.pyler import EulerProblem


class Problem0008(EulerProblem):
    """
    The four adjacent digits in the 1000-digit number that have the greatest
    product are 9 × 9 × 8 × 9 = 5832.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450 Find the thirteen
    adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?
    """

    problem_id = 8
    simple_input = 4
    simple_output = 5832
    real_input = 13
    real_output = 23514624000

    d = """
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    """.replace(
        "\n", ""
    ).replace(
        " ", ""
    )

    def solver(self, input_val):
        max_product = 1
        for x in range(len(self.d) - input_val + 1):
            product = reduce(mul, [int(self.d[x + y]) for y in range(input_val)])
            if product > max_product:
                max_product = product
        return max_product

    def solver2(self, input_val):
        """
        https://projecteuler.net/thread=8&page=5#335894
        You don't have to iterate with a sliding window over the whole number. Any 13-digit sequence including the
        number 0 will always return a product of 0, so you can safely assume that 0 must be excluded from any possible
        sequence. Break the large number up into a series of smaller numbers using 0 as the delimiter,
        and then discard any results that are fewer than 13 digits long.
        """
        num_str_list = self.d.split('0')
        num_list = [[int(i) for i in num] for num in num_str_list if len(num) >= input_val]

        max_product = 0
        for sub_list in num_list:
            sub_list_max_prod = 0
            for x in range(len(sub_list) - input_val + 1):
                product = reduce(mul, [sub_list[x + y] for y in range(input_val)])
                if product > sub_list_max_prod:
                    sub_list_max_prod = product
            if sub_list_max_prod > max_product:
                max_product = sub_list_max_prod
        return max_product


if __name__ == "__main__":
    import unittest
    unittest.main()
