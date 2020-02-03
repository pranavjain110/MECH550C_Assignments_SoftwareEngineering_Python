class ComplexNumbers:
    __r = 0
    __i = 0

    def __init__(self,mat , i, j):
        self.__r[i] = realpart
        self.__i = imagpart
    # https://docs.python.org/3/tutorial/classes.html

    def read(self):
        __number = (self.__r, self.__i)
        return(__number)


    def list2mat(self, r, c, matrix):

        array = [[(0, 0) for i in range(c)] for j in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                array[i][j] = matrix[k].read()
                k = k+1
        return array


    def complexMul(complex1, complex2):
        re = 0
        im = 0
        re = (complex1[0]*complex2[0])-(complex1[1]*complex2[1])
        im = (complex1[1]*complex2[0])+(complex1[0]*complex2[1])
        return (re, im)


    def complexAdd(complex1, complex2):
        re = 0
        im = 0
        re = complex1[0] + complex2[0]
        im = complex1[1] + complex2[1]
        return (re, im)

    def multiplyMat(listA, listB):
        


        row1 = len(matrix1)
        col1 = len(matrix1)
        row2 = len(matrix2)
        col2 = len(matrix2)

        if(col1 == row2):
            print("matrices can be multiplied")
        result = [[(0, 0) for i in range(col2)] for j in range(row1)]

        print(result)
        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    #result[i][j] = matrix1[i][k]*matrix2[k][j]
                    print("i= %d j=%d k=%d" % (i, j, k))
                    result[i][j] = complexAdd(result[i][j], complexMul(matrix1[i][k], matrix2[k][j]))

        print(result)


    


# Create an matrix of size rows x columns consisting of tuples
rows, cols = (2, 2)
list1 = ComplexNumbers([(1, 1), (2, 0), (0, 0), (2, 5)], 2, 2)
list2 = [(5, -5), (0, -2), (0, 4.2), (-11.1, 0)]

ComplexNumbers.multiplyMat(list1, list2)

# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
# arr[1][1][0] calls first and second element of the tuple present in the array
