from pyler import EulerProblem


class Problem0158(EulerProblem):
    """
    Taking three different letters from the 26 letters of the alphabet,
    character strings of length three can be formed. Examples are 'abc', 'hat'
    and 'zyx'. When we study these three examples we see that for 'abc' two
    characters come lexicographically after its neighbour to the left.  For
    'hat' there is exactly one character that comes lexicographically after its
    neighbour to the left. For 'zyx' there are zero characters that come
    lexicographically after its neighbour to the left. In all there are 10400
    strings of length 3 for which exactly one character comes lexicographically
    after its neighbour to the left. We now consider strings of n ≤ 26 different
    characters from the alphabet.  For every n, p(n) is the number of strings of
    length n for which exactly one character comes lexicographically after its
    neighbour to the left. What is the maximum value of p(n)?
    """
    problem_id = 158
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

