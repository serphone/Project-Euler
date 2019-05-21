from pyler import EulerProblem


class Problem0442(EulerProblem):
    """
    An integer is called eleven-free if its decimal expansion does not contain
    any substring representing a power of 11 except 1. For example, 2404 and
    13431 are eleven-free, while 911 and 4121331 are not. Let E(n) be the nth
    positive eleven-free integer. For example, E(3) = 3, E(200) = 213 and
    E(500 000) = 531563. Find E(1018).
    """
    problem_id = 442
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

