# Topic: touch os module in Python
#
# Author: Xuhua Huang
# Last updated: July 26, 2021
# Created on: July 26, 2021

import os
from datetime import datetime


def main():
    cwd = os.getcwd(__file__)
    print(cwd.listdir())

    print(os.stat('fun_os_module.py').st_mtime)
    # covert to human-readable format
    print(datetime.fromtimestamp(os.stat('fun_os_module.py').st_mtime))


if __name__ == '__main__':
    main()
