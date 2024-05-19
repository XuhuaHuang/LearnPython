# Topic: using argparse module for command-line options
# arguments and sub-commands
# Use case: ask user for CLI input with flags and attributes
# Author: Xuhua Huang
#
# Last updated: Aug 13, 2021
# Created on: Aug 13, 2021

"""
Quick Start Guide
Assuming ths file is named 'notes_argparse.py' on the user computer
Run the script with the following command:
$ python notes_argparse.py -h
"""

import argparse

int_parser = argparse.ArgumentParser(description='My customized CLI argument parser')
int_parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='Argument parser to process provided integers')
int_parser.add_argument('-s', '--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers with --sum, default to find the max')

args = int_parser.parse_args()
print(args.accumulate(args.integers))
