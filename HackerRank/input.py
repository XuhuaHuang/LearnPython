# https://www.hackerrank.com/challenges/input/problem

import ast


if __name__ == "__main__":
    x, k = map(int, input().split())
    print(ast.literal_eval(input()) == k)
    """
    eval() function can be used to evaluate the expression.
    The source may be a string representing a Python expression or a code object as returned by compile().
    """
    # print(eval(input()) == k)
