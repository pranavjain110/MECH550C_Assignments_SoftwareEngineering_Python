class ComplexNumbers:
    __r = 0
    __i = 0

    def __init__(self, realpart, imagpart):
        self.__r = realpart
        self.__i = imagpart
    # https://docs.python.org/3/tutorial/classes.html

    def read(self): 
        __number = (self.__r, self.__i)
        return(__number)





def list2mat(r, c, matrix):

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
    re = 0
    im = 0
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
    re = 0
    im = 0
    re = complex1[0] + complex2[0]
    im = complex1[1] + complex2[1]
    return (re, im)

def multiplyMat(matrix1, matrix2):
    """This function is used to multiply to matrices
    
    Arguments:
        matrix1 {list} -- list of all the elements of first matrix
        matrix2 {list} -- list of all the elements of second matrix

    Returns:
        result {list} -- list of elements of the matrix formed after product

    """
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[0])

    if(col1 == row2):
        print("matrices can be multiplied")
    result = [[(0, 0) for i in range(col2)] for j in range(row1)]

    #print(result)
    for i in range(0, row1):
        for j in range(0, col2):
            for k in range(0, col1):
                #result[i][j] = matrix1[i][k]*matrix2[k][j]
                #print("i= %d j=%d k=%d" % (i, j, k))
                result[i][j] = complexAdd(
                    result[i][j], complexMul(matrix1[i][k], matrix2[k][j]))

    return(result)

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
    
# Create an matrix of size rows x columns consisting of tuples
rows, cols = (2, 2)
list1 = [ComplexNumbers(1, 1), ComplexNumbers(2, 0), ComplexNumbers(0, 0), ComplexNumbers(2, 5)]
list2 = [ComplexNumbers(5, -5), ComplexNumbers(0, -2),ComplexNumbers(0, 4.2), ComplexNumbers(-11.1, 0)]

mat1 = list2mat(2, 2, list1)
mat2 = list2mat(2, 2, list2)



print(displayMatrix(mat1))
print(displayMatrix(mat2))


product= multiplyMat(mat1, mat2)
print(displayMatrix(product))

# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/


# arr[1][1][0] calls first and second element of the tuple present in the array
