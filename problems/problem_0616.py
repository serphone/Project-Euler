from pyler import EulerProblem


class Problem0616(EulerProblem):
    """
    Alice plays the following game, she starts with a list of integers $L$ and
    on each step she can either: remove two elements $a$ and $b$ from $L$ and
    add $a^b$ to $L$ or conversely remove an element $c$ from $L$ that can be
    written as $a^b$, with $a$ and $b$ being two integers such that $a, b > 1$,
    and add both $a$ and $b$ to $L$For example starting from the list $L=\{8\}$,
    Alice can remove $8$ and add $2$ and $3$ resulting in $L=\{2,3\}$ in a first
    step. Then she can obtain $L=\{9\}$ in a second step. Note that the same
    integer is allowed to appear multiple times in the list. An integer $n>1$ is
    said to be creative if for any integer $m>1$ Alice can obtain a list that
    contains $m$ starting from $L=\{n\}$.  Find the sum of all creative integers
    less than or equal to $10^{12}$.
    """
    problem_id = 616
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

