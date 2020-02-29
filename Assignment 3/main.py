'''
________________________________________________________________________
Date: February 5, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Asignment Number: 3

Purpose: Multiply two matrices with complex numbers

Description: The program takes a list of tuples representing the real and
the complex part of number forming the matrix and stores it as a private
variable of class ComplexNumber.
Class ComplexMultiplication contains methods to carry out multiplication
of two matrices containg complex numbers

Usage: Run main.exe
________________________________________________________________________
'''


class ComplexNumbers:
    """Class to create a new complex number type
    """
    __r = 0
    __i = 0

    def __init__(self, realpart, imagpart):
        """Constuctor used to initialise the objects of the class
        and its real and imaginary part as private variable

        Arguments:
            realpart {float} -- represents the real part of the complex number
            imagpart {float} -- represents the imaginary part of the complex number
        """
        self.__r = realpart
        self.__i = imagpart

    def read(self):
        """function to read the private variables of the object
        Returns:
            {tuple}-- tuple containing the real and the imaginary part of the number
        """
        __number = (self.__r, self.__i)
        return __number


class ComplexMultiplication:
    """This class contains methods required to carry out muliplication of complex matrices

    """

    def __init__(self, listMat1, listMat2, rowMat1, colMat1, rowMat2, colMat2):
        """This constructor which is used to set argument values
        for the objects and find the product of the matrices

        Arguments:
            listMat1 {list} -- list containing elements of matrix 1
            listMat2 {list} -- list containing elements of matrix 2
            rowMat1 {int} -- number of rows in matrix 1
            colMat1 {int} -- number of columns in matrix 1
            rowMat2 {int} -- number of rows in matrix 2
            colMat2 {int} -- number of rows in matrix 2
        """

        def list2mat(r, c, matrix):
            """This method converts a list containg tuples of length = r*c  into
            a list of length r where each element of the list contains c tuples

            Arguments:
                r {int} -- number of rows of matrix to be formed
                c {int} -- number of columns of the matrix to be formed
                matrix {list} -- list of length  r*c

            Returns:
                array {list} -- variable called array contains a list representing matrix
            """

            array = [[(0, 0) for i in range(c)] for j in range(r)]
            k = 0
            for i in range(r):
                for j in range(c):
                    array[i][j] = matrix[k].read()
                    k = k+1
            return array

        def complexMul(complex1, complex2):
            """This method is used to multiply two complex numbers

                Arguments:
                    complex1 {tuple} -- tuple of 2 representing the real and imaginary part
                    complex2 {tuple} -- tuple of 2 representing the real and imaginary part

                Returns:
                    tuple-- tuple of 2 elements containg the real and the imaginary part
                """
            #  re and im are the real and the complex part of a number
            re = (complex1[0]*complex2[0])-(complex1[1]*complex2[1])
            im = (complex1[1]*complex2[0])+(complex1[0]*complex2[1])
            return (re, im)

        def complexAdd(complex1, complex2):
            """This method is used to add 2 complex numbers

                Arguments:
                    complex1 {tuple} -- tuple of 2 representing the real and imaginary part
                    complex2 {tuple} -- tuple of 2 representing the real and imaginary part

                Returns:
                    tuple -- tuple of 2 elements containg the real and the imaginary part
                """
            # re and im are the real and the complex part of a number
            re = complex1[0] + complex2[0]
            im = complex1[1] + complex2[1]
            return (re, im)

        def multiplyMat():
            """This method is used to multiply two matrices

            Returns:
                result {list} --  list of elements of the matrix formed after product
            """
            # creates and empty 2d list with ech of its element being a tuple
            result = [[(0, 0) for i in range(colMat2)] for j in range(rowMat1)]

            # logic to multiply two matrices
            for i in range(0, rowMat1):
                for j in range(0, colMat2):
                    for k in range(0, colMat1):
                        result[i][j] = complexAdd(
                            result[i][j], complexMul(self.matrix1[i][k], self.matrix2[k][j]))
            return result

        # Condition to check if dimention of matrices are entered as integers
        if not (isinstance(rowMat1, int) and isinstance(colMat1, int) and
                isinstance(rowMat2, int) and isinstance(colMat2, int)):
            print(
                "\n\nPlease ensure that the dimension of the Matrices are positive integers\n\n")
            quit()

        # Condition to check the dimensions of matrices entered are positive
        if rowMat1 < 1 or colMat1 < 1 or rowMat2 < 1 or colMat2 < 1:
            print("\n\nNumber of rows or column cannot be less than 1\n\n")
            quit()

        # Condition to check if the matries can be multplied
        if colMat1 != rowMat2:
            print("\n\nIncorrect dimensions for matrix multiplication. Ensure that the number of " +
                  "columns in the first matrix matches the number of rows in the second matrix.\n")
            quit()

        # Conditions to ensure that the number of elements
        # in a matrix match the product of its row and column
        if len(listMat1) != rowMat1*colMat1:
            print("\n\nEnsure that the number of elements entered in matrix 1 are equal " +
                  "to the product of specified number of rows and columns of the matrix.\n\n")
            quit()
        if len(listMat2) != rowMat2*colMat2:
            print("\n\nEnsure that the number of elements entered in matrix 2 are equal " +
                  "to the product of specified number of rows and columns of the matrix.\n\n")
            quit()

        self.matrix1 = list2mat(rowMat1, colMat1, listMat1)
        self.matrix2 = list2mat(rowMat2, colMat2, listMat2)
        self.rowMat1 = rowMat1
        self.cowMat1 = colMat1
        self.rowMat2 = rowMat2
        self.colMat2 = colMat2
        self.product = multiplyMat()


# Functions

def displayComplexMatrix(matrixToDisplay):
    """This method takes in a list of tuples representing a matix and converts it into a string

    Arguments:
        matrixToDisplay {list} -- list containing all the elements of a matrix

    Returns:
        str -- input matrix conveted to a string
    """
    output = ""
    for i in range(len(matrixToDisplay)):
        for j in range(len(matrixToDisplay[0])):
            output += (str(round(matrixToDisplay[i][j][0], 3)) + " " + \
                "+"*(matrixToDisplay[i][j][1] >= 0) + \
                str(matrixToDisplay[i][j][1]) + "i").ljust(20)
            #output= output.ljust(25)
        output = output + "\n"
    return output


def display(mat1, mat2, resultMat):
    """This functions is used to print the two matrices to be multiplied and their product

    Arguments:
        mat1 {list} -- list containing the 1st matrix
        mat2 {lsit} -- list containing the 2nd matrix
        resultMat {list} -- list containing the product of matrices
    """
    print("1st Matrix is: ")
    print(displayComplexMatrix(mat1))
    print("2nd Matrix is: ")
    print(displayComplexMatrix(mat2))
    print("Product of the matrices is:")
    print(displayComplexMatrix(resultMat))
    print("--------------------------------------")


# --------------------------------------------------------
# The code starts here
# ---------------------------------------------------------


# 2x2 Matrices given in the assignment
# ----------------------------------------------------------------------------------
# represents rows and columns of the first and the second matrix to be multiplied
row1, col1 = 2, 2
row2, col2 = 2, 2

# listA and listB represent the elements of the 1st and 2nd matrix to be multiplied
listA = [(1, 1), (2, 0), (0, 0), (2, 5)]
listB = [(5, -5), (0, -2), (0, 4.2), (-11.1, 0)]
list1, list2 = list(), list()

for var in listA:
    list1.append(ComplexNumbers(var[0], var[1]))
for var in listB:
    list2.append(ComplexNumbers(var[0], var[1]))

CM1 = ComplexMultiplication(list1, list2, row1, col2, row1, col2)
display(CM1.matrix1, CM1.matrix2, CM1.product)

# Matrices of dimentions 2x3 and 3x2 aare multiplied below
# ----------------------------------------------------------------------------------
# represents rows and columns of the first and the second matrix to be multiplied
row3, col3 = 2, 3
row4, col4 = 3, 2

# listA and listB represent the elements of the 1st and 2nd matrix to be multiplied
listA = [(1, 1), (2, 0), (0, 0), (2, 5), (0, 0), (2, 5)]
listB = [(5, -5), (0, -2), (0, 4.2), (-11.1, 0), (0, 4.2), (-11.1, 0)]
list3, list4 = list(), list()

for var in listA:
    list3.append(ComplexNumbers(var[0], var[1]))
for var in listB:
    list4.append(ComplexNumbers(var[0], var[1]))

CM2 = ComplexMultiplication(list3, list4, row3, col3, row4, col4)
display(CM2.matrix1, CM2.matrix2, CM2.product)

# Matrices of dimentions 2x2 and 2x2 aare multiplied below
# -----------------------------------------------------------------------------------
# represents rows and columns of the first and the second matrix to be multiplied
row5, col5 = 2, 2
row6, col6 = 2, 2

# listA and listB represent the elements of the 1st and 2nd matrix to be multiplied
listA = [(2, 2), (4, 6), (5, 5), (4, 10)]
listB = [(10, -10), (2, -4), (2, 8.4), (-22.2, 0)]
list5, list6 = list(), list()

for var in listA:
    list5.append(ComplexNumbers(var[0], var[1]))
for var in listB:
    list6.append(ComplexNumbers(var[0], var[1]))

CM3 = ComplexMultiplication(list5, list6, row5, col5, row6, col6)
display(CM3.matrix1, CM3.matrix2, CM3.product)

# input() command is used to exit the program when the users presses enter
input("\n\nPress Enter to Exit\n\n ")
