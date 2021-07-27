"""
Magic Attributes

Xuhua Huang
Last updated: July 26, 2021

TODO: more on Cython functions and definitions
"""

# 1) compiled - special variable
#    set to True when the compiler runs, and False in the interpreter
import cython

if cython.compiled:
        print(f"{__file__} is compiled!")  # will print this in a .pxd file
else:
        print(f"{__file__} is being interpreted.")  # this line will print since we are in the .py file

# 2) cython.declare declares a typed variable in the current scope
#    usecases: assignment and function call
# assignment usecase:
var_int = cython.declare(cython.int)  # cdef int x
var_flt = cython.declare(cython.float, 3.14159)  # cdef float var_flt = 3.14159
# function call use case:
cython.declare(x=cython.int, y=cython.double)

"""
Some other useful Cython decorators:
@cython.cfunc
@cython.returns(<reutrn_type>)
@cython.final  # prevents inheriting from this class
"""
@cython.cclass  # creates a cdef class
class CStylePoint:
        cython.declare(_x=cython.int, _y=cython.int)  # _x and _y are set to private attribute by default

        def __init__(self, x=0, y=0):
            self._x = x
            self._y = y

        @cython.returns(cython.NULL)
        def __repr__(self):
                print(f"x={self._x}, y={self._y}")
