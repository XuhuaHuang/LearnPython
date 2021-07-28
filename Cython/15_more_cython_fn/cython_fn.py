"""
More on Cython function in pure Python code

Xuhua Huang
Last updated: July 27, 2021
"""

import cython

# 1) declare a pointer as if we are in C and C++
cython.declare(x=cython.int, x_ptr=cython.p_int)
x_ptr = cython.address(x)  # p_int = &x;

# 2) evaluates the size of an element - type and expression
cython.declare(n=cython.longlong)
print(cython.typeof(n))

# 3) create custom struct types
MyStruct = cython.struct(x=cython.int, y=cython.int, data=cython.double)
a = cython.declare(MyStruct)
""" This is equivalent to the following code:
cdef struct MyStruct:
    int x
    int y
    double data

cdef Mystrcut a
"""

# 4) working with typedef(s)
T = cython.typedef(cython.p_int)  # now T is the data type of integer pointer
# ctypedef int* T
