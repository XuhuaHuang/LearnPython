# Topic: Notes on iterator in Python
# File: iterator.py
# if in class: __iter__ and __next__
# Author: Xuhua Huang
#
# Last updated: Nov 4, 2021
# Created on: Nov 4, 2021

def main():
    int_list: list[int] = [0, 1, 2, 3, 4, 5]
    for i in int_list:
        print(i);

    # define a list of string and obtain the iterator
    people: list[str] = ['Andy', 'Andrew', 'Liam']
    iter_people = iter(people)
    print(f'Printing the object iter_people: {iter_people}')
    print(f'Printing the object type: {type(iter_people)}')

    print(next(iter_people))
    print(next(iter_people))
    print(next(iter_people))
    # print(next(iter_people)) #StopIteration



if __name__ == '__main__':
    main()