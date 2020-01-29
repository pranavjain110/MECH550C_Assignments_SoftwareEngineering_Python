# ---------------------------------------------------------------
# Author: Pranav Jain
# Date: January 28, 2020
# Student Number = 14213029
# Source File: main.py
#
# Course: MECH 550C - Software Design
# Asignment Number: 2
#
# Purpose: Compare area of two rectangles
#
# Description:
# This program compares area of two rectangles and prints True
# if the area is equal and False if the area is different
#
# Usage: Run main.exe
# ----------------------------------------------------------------


def rectangleArea(l, w):
    """This is a function to calculate the area of a rectangle

    Arguments:
        l  -- length of the rectangle
        w  -- width of a rectangle

    Returns:
        a -- Area of the rectangle
    """
    a = l*w
    return a


length1 = 2.6
width1 = 10

length2 = 13
width2 = 2

rectArea1 = rectangleArea(length1, width1)
rectArea2 = rectangleArea(length2, width2)

x = (rectArea1 == rectArea2)

print(x)

#input() command is used to exit the program when the users presses enter
input("\nPress Enter to Exit ")
