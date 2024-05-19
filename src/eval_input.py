# https://www.hackerrank.com/challenges/input/problem

"""
eval() function can be used to evaluate the expression.
The source may be a string representing a Python expression or a code object returned by compile().
"""

import ast


if __name__ == "__main__":
    x, k = map(int, input().split())
    print(ast.literal_eval(input()) == k)
    # print(eval(input()) == k)
