# Topic: Interview test via Teams and screen share
#
# Author: Xuhua Huang
# Last updated: Oct 20, 2021
# Created on: Oct 20, 2021

from Util import lookupvalue


def main():
    for i in range(100):
        # Define content marcos
        fizz_str: str = "Fizz"
        buzz_str: str = "Buzz"
        fizz_buzz_str: str = "Fizz Buzz"
        result: str = str(i)
        # Enter control flow
        if i % 3 == 0 and i % 5 == 0:
            result = fizz_buzz_str
        elif i % 3 == 0:
            result = fizz_str
        elif i % 5 == 0:
            result = buzz_str

        print(result)


if __name__ == '__main__':
    main()
