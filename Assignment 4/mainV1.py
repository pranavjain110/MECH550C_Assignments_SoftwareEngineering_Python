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

    def __add__(complex1, complex2):
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

    def complexSubtract(complex1, complex2):
        
        """This method is used to add 2 complex numbers

        Arguments:
            complex1 {tuple} -- tuple of 2 representing the real and imaginary part
            complex2 {tuple} -- tuple of 2 representing the real and imaginary part

        Returns:
            tuple -- tuple of 2 elements containg the real and the imaginary part
        """

        re = complex1[0] - complex2[0]
        im = complex1[1] - complex2[1]
        return (re, im)


    def multiplyMat(listMat1,listMat2, rowMat1, colMat1, rowMat2, colMat2):

        """This method is used to multiply two matrices

        Returns:
            result {list} --  list of elements of the matrix formed after product
        """
        
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

        matrix1 = ComplexNumbers.list2mat(rowMat1, colMat1, listMat1)
        matrix2 = ComplexNumbers.list2mat(rowMat2, colMat2, listMat2)
        
        # creates and empty 2d list with ech of its element being a tuple
        result = [[(0, 0) for i in range(colMat2)] for j in range(rowMat1)]

        # logic to multiply two matrices
        for i in range(0, rowMat1):
            for j in range(0, colMat2):
                for k in range(0, colMat1):
                    result[i][j] = result[i][j] + ComplexNumbers.complexMul(matrix1[i][k], matrix2[k][j])
        return result


#___________________________________________________________________________________________________





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

print(ComplexNumbers.multiplyMat(list1,list2,2,2,2,2))
