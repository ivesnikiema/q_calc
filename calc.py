import sys
import re
import operator
from functools import reduce

non_digit_matcher = re.compile(r'\D')
expr_matcher = re.compile(r'(\w+ \d+ \d+)')
operations = {'add': operator.add,
              'multiply': operator.mul}


def solve(expr: str) -> str:
    """
    Given an expression, this function recursively solves the expression and returns the result

    :param expr: str representing the expression to solve e.g "(add 1 2)" or "123"
    :return: the result of the expression in str
    """

    if not non_digit_matcher.search(expr):
        return expr
    expr_match = expr_matcher.search(expr)
    op, *exps = expr_match.group(1).split(' ')
    assert op in operations, f'{op} operation is not supported. Use either add or multiply'
    result = reduce(operations[op], map(int, exps))
    arg = expr.replace(f'({expr_match.group(1)})', str(result))
    return solve(arg)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('The program was invoked with invalid arguments.\ntry python calc.py \"(add 1 2)\"')
    else:
        print(solve(sys.argv[1]))
