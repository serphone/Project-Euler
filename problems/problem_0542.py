from pyler import EulerProblem


class Problem0542(EulerProblem):
    """
    Let S(k) be the sum of three or more distinct positive integers having the
    following properties: No value exceeds k. The values form a geometric
    progression. The sum is maximal.S(4) = 4 + 2 + 1 = 7S(10) = 9 + 6 + 4 = 19S(
    12) = 12 + 6 + 3 = 21S(1000) = 1000 + 900 + 810 + 729 = 3439 Let $T(n) =
    \sum_{k=4}^n (-1)^k S(k)$.T(1000) = 2268 Find T(1017).
    """
    problem_id = 542
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

