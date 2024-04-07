# File: add_str_integers.py
# Author: TODO
# Date: TODO
# Description: Sovling the adding large number problem
#              by using strings.

from comp120 import Stack, EmptyStructureError


def add_str_integers(num1: str, num2: str) -> str:
    """
    implement the algorithm with 3 stacks.
    """
    # TODO
    return ''  # Replace this line with your code.


def main():
    """ 
    orchestrate the process
    """
    expressions = [
        '592 + 3784', '3456 + 6789', '18274364583 + 8129498165026350236'
    ]
    expected = [
        '592 + 3784 = 4376', '3456 + 6789 = 10245',
        '18274364583 + 8129498165026350236 = 8129498183300714819'
    ]
    your_results = []
    for expression in expressions:
        n1, _, n2 = expression.split()
        r = add_str_integers(n1, n2)
        your_results.append(expression + ' = ' + r)
    print('\nExpected output:')
    for r in expected:
        print(r)
    print('\nYour output:')
    for l in your_results:
        print(l)
    if your_results == expected:
        print("\nAll tests passed. ")
    else:
        print("\nBug in your code. Keep working on it.")


if __name__ == "__main__":
    main()
