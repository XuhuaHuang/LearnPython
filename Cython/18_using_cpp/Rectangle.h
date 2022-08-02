/*****************************************************************//**
 * \file   Rectangle.h
 * \brief  contains declaration for Shapes::Rectangle
 * 
 * \author Xuhua Huang
 * \date   August 13, 2021
 *********************************************************************/

#ifndef RECTANGLE_H
#define RECTANGLE_H

namespace Shapes {
class Rectangle {
public:
    int x0, y0, x1, y1;

    // Default/overloaded constructor and destructor
    Rectangle();
    Rectangle(int x0, int y0, int x1, int y1);
    ~Rectangle();

    // Member functions
    int getArea();
    void getSize(int* width, int* height);
    void move(int dx, int dy);
} Rectangle;

} // namespace Shapes

#endif
