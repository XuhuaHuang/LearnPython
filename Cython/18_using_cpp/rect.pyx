# distutils: language = c++

"""
Working with C++ in Cython
Official tutorial: https://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html
Xuhua Huang
Last updated: 21:11, Aug 14, 2021
"""

from Rectangle cimport Rectangle

def main():
    rec_ptr = new Rectangle(1, 2, 3, 4)  # instantiate a Rectangle object on the heap
    try:
        rec_area = rec_ptr.getArea()
        print(f"The area of created rectangle is: {rec_area}.")
    finally:
        del rec_ptr

    cdef Rectangle rec_stack  # instantiate a Rectangle object on the stack


if __name__ == '__main__':
    main()

# TODO: Create a Cython wrapper class