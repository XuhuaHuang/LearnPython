"""
safe and automatic memory management of Python
with built-in `array` module in Python and Cython

Xuhua Huang
Last updated: 21:01, July 28, 2021
"""

from cpython cimport array  # cython
import array  # python
from libc.string cimport memset

# 1) safe usage with memory views ----------------------------------------------
"""
import brings the regular Python array object into the namespace
and cimport adds functions accessible from Cython
"""
cdef array.array my_int_arr = array.array('i', [1, 2, 3, 4, 5])
cdef int[:] my_arr_copy = my_int_arr

print(f"The first element in the array copy: {my_arr_copy[0]}")

# 2) memory  views with defined function ---------------------------------------
cdef int overhead(object arr):  # can think of this as parse by copy
    cdef int[:] cp_arr = arr
    return cp_arr[0]

cdef int no_overhead(int[:] cp_arr):  # can think of this as parse by reference
    return cp_arr[0]

print("Working wit memory views:")
print("Printing the complete array: ", my_int_arr[:])
print("Function parses by copy", overhead(my_int_arr))  # new memory allocated
print("Function parses by reference", no_overhead(my_int_arr))

# 3) zero-overhead, unsafe access to raw C pointers ----------------------------
# access underlaying C pointers
print("Accessing underlaying pointer of constructed integer pointer",
      my_int_arr.data.as_ints[0])
memset(my_int_arr.data.as_voidptr, 0, len(my_int_arr)*sizeof(int))

# 4) cloning and extending arrays ----------------------------------------------
cdef array.array arr_ext = array.array('i', [6, 7, 8, 9, 10])
# extend my_int_arr with arr_ext, resizes as needed
array.extend(my_int_arr, arr_ext)
array.resize(my_int_arr, len(my_int_arr)-len(arr_ext))
print("Size of extended array \"my_int_arr\": ", len(my_int_arr))
print("Printing extended array \"my_int_arr\": ", my_int_arr[:])

# 5) some of the BUILT_IN useful function prototypes/signatures ----------------
"""
cdef int resize(array self, Py_ssize_t n) except -1

cdef int resize_smart(array self, Py_ssize_t n) except -1

cdef inline array clone(array template, Py_ssize_t length, bint zero)
    # Efficient for small increments
    # uses growth pattern that delivers amortized linear-time appends

cdef inline int extend_buffer(array self, char* stuff, Py_ssize_t n) except -1
    # Make a copy of an array

cdef inline void zero(array self)
    # Extend array with data from another array with the same type

"""
