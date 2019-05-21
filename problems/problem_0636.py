from pyler import EulerProblem


class Problem0636(EulerProblem):
    """
    Consider writing a natural number as product of powers of natural numbers
    with given exponents, additionally requiring different base numbers for each
    power. For example, $256$ can be written as a product of a square and a
    fourth power in three ways such that the base numbers are different. That
    is, $256=1^2\times 4^4=4^2\times 2^4=16^2\times 1^4$ Though $4^2$ and $2^4$
    are both equal, we are concerned only about the base numbers in this
    problem. Note that permutations are not considered distinct, for example
    $16^2\times 1^4$ and $1^4 \times 16^2$ are considered to be the same.
    Similarly, $10!$ can be written as a product of one natural number, two
    squares and three cubes in two ways ($10!=42\times5^2\times4^2\times3^3\time
    s2^3\times1^3=21\times5^2\times2^2\times4^3\times3^3\times1^3$) whereas
    $20!$ can be given the same representation in $41680$ ways. Let $F(n)$
    denote the number of ways in which $n$ can be written as a product of one
    natural number, two squares, three cubes and four fourth powers. You are
    given that $F(25!)=4933$, $F(100!) \bmod 1\,000\,000\,007=693\,952\,493$,
    and $F(1\,000!) \bmod 1\,000\,000\,007=6\,364\,496$. Find $F(1\,000\,000!)
    \bmod 1\,000\,000\,007$.
    """
    problem_id = 636
    simple_input = 0
    simple_output = 1
    real_input = 0
    real_output = 1
    
    @staticmethod
    def solver(input_val):
        raise NotImplementedError


if __name__ == '__main__':
    import unittest
    unittest.main()

