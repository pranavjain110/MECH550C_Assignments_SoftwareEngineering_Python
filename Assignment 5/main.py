'''
________________________________________________________________________
Date: February 19, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Assignment Number: 5

Purpose: Multiply two matrices with exception handling

Description: This code demonstrates the concepts of Classes and Function
Overloading to multiply and display complex numbers.
The program  takes in inputs from the user, validates it and handles the
exceptions using try-except-else block.

Usage: Run main.exe
________________________________________________________________________
'''

import math
import sys
import gc


class ComplexNumbers:
    """Class to create a new complex number type
    """
    __r = 0
    __i = 0

    def __init__(self, realpart, imagpart):
        """Constructor used to initialise the objects of the class
        and its real and imaginary part as private variable

        Arguments:
            realpart {float} -- represents the real part of the complex number
            imagpart {float} -- represents the imaginary part of the complex number
        """
        self.__r = realpart
        self.__i = imagpart

    def __del__(self):
        """Destructor to delete class objects and its class members
        """

        if 'pydevd' in sys.modules:
            print("\n[D1] From destructor in ComplexNumber : ")
            print('|Destructor called, object of class ComplexNumber deleted|')
            print("len(gc.get_objects):", len(gc.get_objects()))
            print("gc.get_stats:", gc.get_stats())
            print("gc.get_count:", gc.get_count())

    def __str__(self):
        """Method overloading to print a complex number in a+bi string format

        Returns:
           string -- string contains complex number in a+bi format
        """
        output = ""
        if self.read()[0] > 0:
            sign1st = ""
        elif self.read()[0] == 0:
            sign1st = ""
        else:
            sign1st = "-"

        if self.read()[1] > 0:
            sign2nd = "+"
        elif self.read()[1] == 0 or self.read()[0] == 0:
            sign2nd = ""
        else:
            sign2nd = "-"
        readFuncType = self.read

        if readFuncType()[0] == 0:
            arg1 = ""
        else:
            arg1 = abs(readFuncType()[0])

        if readFuncType()[1] == 0:
            arg2 = ""
            imSym = ""
        else:
            arg2 = abs(readFuncType()[1])
            imSym = "i"

        if readFuncType()[0] == 0 and readFuncType()[1] == 0:
            arg1 = "0"

        output += "{0}{1}{2}{3}{4}".format(sign1st, arg1, sign2nd, arg2, imSym)
        return output

    def read(self):
        """function to read the private variables of the object
        Returns:
            {tuple}-- tuple containing the real and the imaginary part of the number
        """
        __number = (self.__r, self.__i)
        return __number

    def returnPolar(self):
        """function to read the private variables of the object and returnnumber in polar form

        Returns:
            {tuple} -- tuple containing Absolute value and phase of a polar number
        """
        absValue = math.sqrt((self.__r**2)+(self.__i**2))
        phase = math.atan2(self.__i, self.__r)
        return (absValue, phase)

    def __mul__(self, num2):
        """This is an overloaded method is used to multiply two complex numbers

        Arguments:
            num2 {ComplexNumbers} -- object of class ComplexNumbers

        Returns:
           {ComplexNumbers} -- object of class ComplexNumbers
        """

        complex1 = self.read()
        complex2 = num2.read()
        re = (complex1[0]*complex2[0])-(complex1[1]*complex2[1])
        im = (complex1[1]*complex2[0])+(complex1[0]*complex2[1])
        return ComplexNumbers(re, im)

    def __add__(self, compNum2):
        """This method is used to add 2 complex numbers input as an object of class ComplexNumbers

        Arguments:
            compNum2 {ComplexNumbers} -- object of class ComplexNumbers

        Returns:
           {ComplexNumbers} -- object of class ComplexNumbers
        """
        # re and im are the real and the complex part of a number
        complex1 = self.read()
        complex2 = compNum2.read()
        re = complex1[0] + complex2[0]
        im = complex1[1] + complex2[1]

        return ComplexNumbers(re, im)

    def __sub__(self, compNum2):
        """This method is used to subtact 2 complex numbers input as an
        object of class ComplexNumbers

        Arguments:
            compNum2 {ComplexNumbers} -- object of class ComplexNumbers

        Returns:
           {ComplexNumbers} -- object of class ComplexNumbers
        """
        # re and im are the real and the complex part of a number
        complex1 = self.read()
        complex2 = compNum2.read()
        re = complex1[0] - complex2[0]
        im = complex1[1] - complex2[1]

        return ComplexNumbers(re, im)


class ComplexMultiplication:
    """This matrix is used to store each variable of a list contains tuples, representing elements
    of a matrix as an object of class ComplexNumbers and Carry out the multiplication of 2 matrices

    Returns:
        {list} -- each element of the list is an object of class ComplexNumbers
    """

    def __init__(self, listOfElements, row, col):

        self.listMat = []
        self.row = row
        self.col = col
        k = 0
        for i in range(row):
            tempList = []
            for j in range(col):
                tempList.append(ComplexNumbers(
                    listOfElements[k][0], listOfElements[k][1]))
                k += 1
            self.listMat.append(tempList)
        self.result = []

    def __del__(self):
        """Destructor to delete class objects and its class members
        """

        # Code taken from:
        # https://stackoverflow.com/questions/333995/how-to-detect-
        # that-python-code-is-being-executed-through-the-debugger
        if 'pydevd' in sys.modules:
            print("\n[D2] from destructor in ComplexMultiplication: ")
            print('|Destructor called, object of class ComplexMultiplication deleted|')
            print("len(gc.get_objects):", len(gc.get_objects()))
            print("gc.get_stats:", gc.get_stats())
            print("gc.get_count:", gc.get_count())

    def multiplyMat(self, mat2):
        """This method is used to multiply two matrices

        Returns:
            result {list} --  list of elements of the matrix formed after product
        """

        # creates and empty 2d list with each of its element being a tuple
        self.result = [[ComplexNumbers(0, 0) for i in range(
            mat2.col)] for j in range(self.row)]

        # logic to multiply two matrices
        for i in range(0, self.row):
            for j in range(0, mat2.col):
                for k in range(0, self.col):
                    self.result[i][j] = self.result[i][j] + \
                        (self.listMat[i][k] * mat2.listMat[k][j])
        return self.result


# Function to form a string to display Complex Matrices
def displayComplexMatrix(matrixToDisplay):
    """This method takes in a list of tuples representing a matrix
    and converts it into a string

    Arguments:
        matrixToDisplay {list} -- list containing all the elements
        of a matrix as object of class ComplexNumbers

    Returns:
        strOutput -- input matrix converted to a string
    """

    strOutput = ""
    for i in range(len(matrixToDisplay)):
        for j in range(len(matrixToDisplay[0])):

            strOutput += (str(matrixToDisplay[i][j])).ljust(20)
        strOutput = strOutput + "\n"
    return strOutput


# Function to display matrices and their product
def display(mat1, mat2, resultMat):
    """This functions is used to print the two matrices to be multiplied and their product

    Arguments:
        mat1 {list} -- list containing the 1st matrix
        mat2 {list} -- list containing the 2nd matrix
        resultMat {list} -- list containing the product of matrices
    """

    print("\n1st Matrix is: ")
    print(displayComplexMatrix(mat1))
    print("2nd Matrix is: ")
    print(displayComplexMatrix(mat2))
    print("Product of the matrices is:")
    print(displayComplexMatrix(resultMat))
    print("__________________________________________")


# -----------------------Assignment 5: Main Program Starts Here---------------------------------

def posIntInput(string):
    """Function to ensure that the input is a positive integer

    Arguments:
        string {str} -- string to print while taking input from user
    """
    while True:
        try:
            while True:
                value = int(input(string))
                if value > 0:
                    break
                else:
                    print("Please enter a positive integer.\n")

            break
        except ValueError:
            print("\nError: That is not an integer")
            print("Press Enter to input the value again.\n")
    return value


def floatInput(string):
    """Function to ensure that the input is a number of type float

    Arguments:
        string {str} -- string to print while taking input from user
    """
    while True:
        try:
            value = float(input(string))
            break
        except ValueError:
            print("\nError: That is not a valid float number")
            print("Press Enter to input the value again!!\n")
    return value


def multiplyMatrices():
    """Function carries out matrix multiplication by using various methods
    defined in class ComplexNumbers and ComplexMultiplication

    Returns:
        None
    """
    def listOfTuples(row, col):
        """Takes input of real and imaginary part of a complex number and
        forms a list of tuples. Where each tuple represents an object of
        class ComplexNumber

        Arguments:
            row {int} --rows of the matrix to be formed
            col {int} -- columns of the matrix to be formed

        Returns:
            list -- list of objects of class ComplexNumbers
        """

        matList = []
        for i in range(row):
            for j in range(col):
                re = floatInput(
                    "Enter the Real part of element({},{}): ".format(i+1, j+1))
                im = floatInput(
                    "Enter the Complex part({},{}): ".format(i+1, j+1))
                matList.append((re, im))

        listOfObjects = ComplexMultiplication(matList, row, col)
        return listOfObjects, row, col

    row1 = posIntInput("Enter the Number of Rows of the matrix 1:")
    col1 = posIntInput("Enter the Number of Columns of the matrix 1:")
    list1, row1, col1 = listOfTuples(row1, col1)
    while True:
        try:
            row2 = posIntInput("Enter the Number of Rows of the matrix 2:")
            # Condition to check if the matrices can be multiplied
            if row2 != col1:
                raise ValueError()
        except ValueError:
            print("\n\nIncorrect dimensions for matrix multiplication. Ensure that the number of " +
                  "columns in the first matrix matches the number of rows in the second matrix.\n" +
                  "\n\nPlease enter the values again/n/n")

        else:
            col2 = posIntInput("Enter the Number of Columns of the matrix 2:")
            break
    list2, row2, col2 = listOfTuples(row2, col2)

    product = list1.multiplyMat(list2)
    print("_____________________________")
    display(list1.listMat, list2.listMat, product)

    return


def multiplyVectors():
    """Function to take input of two complex numbers and
    print their product
    """

    re = floatInput("Enter the Real part of 1st Vector: ")
    im = floatInput("Enter the Complex part 1st Vector: ")
    v1 = ComplexNumbers(re, im)
    re = floatInput("Enter the Real part of 2nd Vector: ")
    im = floatInput("Enter the Complex part 2nd Vector: ")
    v2 = ComplexNumbers(re, im)
    print("\nProduct of {} and {} = {}\n".format(v1, v2, v1*v2))


while True:
    try:
        print("\nWhat would you like to do today:\n\t1: Matrix Multiplication\
            \n\t2: Vector Multiplication\n\t3: Quit\n")

        switch = posIntInput("Please enter the option number: ")
        if switch == 3:
            break
        if switch < 1 or switch > 3:
            raise ValueError()

    except ValueError:
        print("\nError: That is not a valid option.")
        print("Please enter the value again\n")
    else:
        if switch == 1:
            multiplyMatrices()
        if switch == 2:
            multiplyVectors()

print("\n\tThankyou and have a wonderful day!!!!")

print("\t\tEnd of program")
