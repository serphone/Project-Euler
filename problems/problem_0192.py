from pyler import EulerProblem


class Problem0192(EulerProblem):
    """
    Let x be a real number. A best approximation to x for the denominator bound
    d is a rational number r/s in reduced form, with s ≤ d, such that any
    rational number which is closer to x than r/s has a denominator larger than
    d: |p/q-x| < |r/s-x| ⇒ q > d For example, the best approximation to √13 for
    the denominator bound 20 is 18/5 and the best approximation to √13 for the
    denominator bound 30 is 101/28. Find the sum of all denominators of the best
    approximations to √n for the denominator bound 1012, where n is not a
    perfect square and 1 < n ≤ 100000.
    """
    problem_id = 192
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

