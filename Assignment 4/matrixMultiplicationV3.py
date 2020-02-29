'''
__________________________________________________________________
Author: Pranav Jain
Date: February 4, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Asignment Number: 3

Purpose: Multiply two matrices with complex numbers

Description:


Usage: Run main.exe
__________________________________________________________________
'''


class ComplexNumbers:
    __complexElement = []

    def __init__(self, mat, r, c):
        if len(mat) != r*c:
            print("\n\nEnsure that the number of elements entered are equal " +
                  "to the product of specified number of rows and columns.\n\n")
            quit()
        k = 0
        array = [[(0, 0) for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                array[i][j] = mat[k][0], mat[k][1]
                k = k+1

        for j in range(r):
            self.__complexElement = array
        # https://docs.python.org/3/tutorial/classes.html

    def matrixMul(self, obj2):
        """This function is used to multiply to matrices

        Arguments:
            obj2 {list} -- list of all the elements of a matrix

        Returns:
            result {list} -- list of elements of the ematrix formed after product
        """
        # 1 and 2 in the variable name refer the matrix 1 and matrix 2 respectively
        row1 = len(self.__complexElement)
        col1 = len(self.__complexElement[0])
        col2 = len(obj2.__complexElement[0])
        matrix1 = self.__complexElement
        matrix2 = obj2.__complexElement

        def complexMul(complex1, complex2):
            """This method is used to multiply two complex numbers

            Arguments:
                complex1 {tuple} -- tuple of 2 representing the real and imaginary part
                complex2 {tuple} -- tuple of 2 representing the real and imaginary part

            Returns:
                tuple-- tuple of 2 elements containg the real and the imaginary part
            """

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

            re = complex1[0] + complex2[0]
            im = complex1[1] + complex2[1]
            return (re, im)

        # creates and empty 2d list with ech of its element being a tuple
        result = [[(0, 0) for i in range(col2)] for j in range(row1)]

        # logic to multiply two matrices
        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    result[i][j] = complexAdd(
                        result[i][j], complexMul(matrix1[i][k], matrix2[k][j]))

        return result

    def display(self):
        """This method is used to return the product matrix as a string

        Returns:
            sting -- product matrix stored as a list
        """
        return displayMatrix(self.__complexElement)


def displayMatrix(matrixToDisplay):
    """This method takes in a list of tuples representing a matix and converts it into a string

    Arguments:
        matrixToDisplay {list} -- list containing all the elements of a matrix

    Returns:
        str -- input matrix conveted to a string
    """
    output = ""
    for i in range(len(matrixToDisplay)):
        for j in range(len(matrixToDisplay[0])):
            output += str(matrixToDisplay[i][j][0]) + " " + \
                "+"*(matrixToDisplay[i][j][1] >= 0) + \
                str(matrixToDisplay[i][j][1]) + "i\t\t"
        output = output + "\n"
    return output

# represents rows and columns of the first and the second matrix to be multiplied respectively
row_1, col_1 = 2, 2
row_2, col_2 = 2, 2

# Condition to check the matices have valid dimentions
if row_1 < 1 or col_1 < 1 or row_1 < 1 or col_2 < 1:
    print("\n\nNumber of rows or column cannot be less than 1\n\n")
    quit()

# The two matrix to be multipled are created as objects of the class ComplexNumbers
list1 = ComplexNumbers([(1, 1), (2, 0), (0, 0), (2, 5)], row_1, col_1)
list2 = ComplexNumbers([(5, -5), (0, -2), (0, 4.2), (-11.1, 0)], row_2, col_2)

# Condition to check if the matries can be multplied
if col_1 != row_2:
    print("\n\nIncorrect dimensions for matrix multiplication. Ensure that the number of " +
          "columns in the first matrix matches the number of rows in the second matrix.\n\n")
    quit()
else:
    matProduct = list1.matrixMul(list2)

    print("Matrix 1 is: ")
    print(list1.display())
    print("Matrix 2 is: ")
    print(list2.display())
    print("Product of the matrix is:")
    print(displayMatrix(matProduct))
