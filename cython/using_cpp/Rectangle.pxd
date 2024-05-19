# Declaring a C++ class interface
cdef extern from "Rectangle.h" namespace "Shapes":
    cdef cppclass Rectangle:
        Rectangle() except +
        Rectangle(int, int, int , int) except +
        int x0, x1, y0, y1
        int getArea()
        void getSize(int *width, int *height)
        void move(int, int)
