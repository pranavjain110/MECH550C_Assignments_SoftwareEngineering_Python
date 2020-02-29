import math 

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
    
    def __str__(self,type="RectCoordinate"):
        output=""
        if self.read()[0] > 0:
            sign1st = " "
        elif self.read()[0] == 0:
            sign1st = ""
        else:
            sign1st = "-"

        if self.read()[1] > 0:
            sign2nd = "+"
        elif self.read()[1] == 0:
            sign2nd = ""
        else:
            sign2nd = "-"

        #if type == "RectCoordinate":
        readFuncType = self.read 
        #elif type=="PolarCoordinate":
        #    readFuncType = self.returnPolar   
        
        if readFuncType()[0] ==0:
            arg1=""
        else:
            arg1 = abs(readFuncType()[0])

        if readFuncType()[1] ==0:
            arg2=""
            imSym=""
        else:
            arg2 = abs(readFuncType()[1])
            imSym="i"
        
        if readFuncType()[0] ==0 and readFuncType()[1] ==0:
            arg1="  0 "


        #if type == "RectCoordinate":
            
        output += "{0}{1}{2}{3}{4}\t\t".format(sign1st,arg1,sign2nd,arg2,imSym)

        # elif type=="PolarCoordinate":
        #     output += "{0} {1:.3f} {2} {3}{4:.3f}\t\t".format(sign1st,arg1,u"\u2220",sign2nd,arg2)
        # else:
        #     print("Please enter the right display type of Complex Matrix(RectCoordinate or PolarCoordinate)")

        #print("Output is: {}".format(output))
        return output
        

    def read(self):
        """function to read the private variables of the object
        Returns:
            {tuple}-- tuple containing the real and the imaginary part of the number
        """
        __number = (self.__r, self.__i)
        return __number
    
    def returnPolar(self):
        absValue= math.sqrt((self.__r**2)+(self.__i**2))

        #print("Rea Patr:{}  Complex:{}  Abs{}".format(self.__r,self.__i, absValue))
        phase = math.atan2(self.__i,self.__r)
        return (absValue, phase)  

    def __mul__(self, num2):
        """This method is used to multiply two complex numbers

        Arguments:
            complex1 {tuple} -- tuple of 2 representing the real and imaginary part
            complex2 {tuple} -- tuple of 2 representing the real and imaginary part

        Returns:
            tuple-- tuple of 2 elements containg the real and the imaginary part
        """
        complex1 = self.read()
        complex2 = num2.read()
        re = (complex1[0]*complex2[0])-(complex1[1]*complex2[1])
        im = (complex1[1]*complex2[0])+(complex1[0]*complex2[1])
        return ComplexNumbers(re, im)

    def __add__(self, compNum2):
        """This method is used to add 2 complex numbers

            Arguments:
                complex1 {tuple} -- tuple of 2 representing the real and imaginary part
                complex2 {tuple} -- tuple of 2 representing the real and imaginary part

            Returns:
                tuple -- tuple of 2 elements containg the real and the imaginary part
            """
        # re and im are the real and the complex part of a number
        complex1 = self.read()
        complex2 = compNum2.read()
        re = complex1[0] + complex2[0]
        im = complex1[1] + complex2[1]

        return ComplexNumbers(re, im)

    def __sub__(self, compNum2):
        """This method is used to add 2 complex numbers

            Arguments:
                complex1 {tuple} -- tuple of 2 representing the real and imaginary part
                complex2 {tuple} -- tuple of 2 representing the real and imaginary part

            Returns:
                tuple -- tuple of 2 elements containg the real and the imaginary part
            """
        # re and im are the real and the complex part of a number
        complex1 = self.read()
        complex2 = compNum2.read()
        re = complex1[0] - complex2[0]
        im = complex1[1] - complex2[1]

        return ComplexNumbers(re, im)

class ComplexMultiplication:
    
    def __init__(self,listOfElements,row,col):
        self.listMat = []
        self.row=row
        self.col=col
        k=0
        for i in range (row):
            tempList =[]
            for j in range(col):
                tempList.append(ComplexNumbers(listOfElements[k][0], listOfElements[k][1]))
                k +=1
            self.listMat.append(tempList)
        self.result = []

    
    def multiplyMat(self,mat2):
        """This method is used to multiply two matrices

        Returns:
            result {list} --  list of elements of the matrix formed after product
        """
            # creates and empty 2d list with each of its element being a tuple
        self.result = [[ComplexNumbers(0, 0) for i in range(mat2.col)] for j in range(self.row)]

        # logic to multiply two matrices
        for i in range(0, self.row):
            for j in range(0, mat2.col):
                for k in range(0, self.col):
                    self.result[i][j] = self.result[i][j] + (self.listMat[i][k] *  mat2.listMat[k][j])
        return self.result


def displayComplexMatrix(matrixToDisplay,type):
    """This method takes in a list of tuples representing a matix and converts it into a string

    Arguments:
        matrixToDisplay {list} -- list containing all the elements of a matrix

    Returns:
        str -- input matrix conveted to a string
    """

    strOutput = ""
    for i in range(len(matrixToDisplay)):
        for j in range(len(matrixToDisplay[0])):
            
                strOutput += str(matrixToDisplay[i][j])

    #         if matrixToDisplay[i][j].read()[0] >= 0:
    #             sign1st = " "
    #         else:
    #             sign1st = "-"

    #         if matrixToDisplay[i][j].read()[1] >= 0:
    #             sign2nd = "+"
    #         else:
    #             sign2nd = "-"

    #         if type == "RectCoordinate":
    #             readFuncType = matrixToDisplay[i][j].read 
    #         elif type=="PolarCoordinate":
    #             readFuncType = matrixToDisplay[i][j].returnPolar         
    #         arg1=readFuncType()[0]
    #         arg2 =readFuncType()[1]

    #         if type == "RectCoordinate":
    #             
    #             output += "{0} {1:.2f} {2} {3:.2f}\t\t".format(sign1st,abs(arg1),sign2nd,abs(arg2))

    #         elif type=="PolarCoordinate":
    #             output += "{0} {1:.3f} {2} {3}{4:.3f}\t\t".format(sign1st,abs(arg1),u"\u2220",sign2nd,abs(arg2))


    #         else:
    #             print("Please enter the right display type of Complex Matrix(RectCoordinate or PolarCoordinate)")
        strOutput = strOutput + "\n"
    return strOutput



def display(mat1, mat2, resultMat,type="RectCoordinate"):
    """This functions is used to print the two matrices to be multiplied and their product

    Arguments:
        mat1 {list} -- list containing the 1st matrix
        mat2 {lsit} -- list containing the 2nd matrix
        resultMat {list} -- list containing the product of matrices
    """
             
    print("\n1st Matrix is: ")
    print(displayComplexMatrix(mat1,type))
    print("2nd Matrix is: ")
    print(displayComplexMatrix(mat2,type))
    print("Product of the matrices is:")
    print(displayComplexMatrix(product,type))
    print("--------------------------------------")



# 2x2 Matrices given in the assignment
# ----------------------------------------------------------------------------------
# represents rows and columns of the first and the second matrix to be multiplied
row1, col1 = 2, 2
row2, col2 = 2, 2

# listA and listB represent the elements of the 1st and 2nd matrix to be multiplied
listA = [(1, 1), (2, 0), (0, 0), (2, 5)]
listB = [(5, -5), (0, -2), (0, 4.2), (-11.1, 0)]

list1=ComplexMultiplication(listA,row1,col1)
list2=ComplexMultiplication(listB,row2,col2)
product=list1.multiplyMat(list2)

display(list1.listMat,list2.listMat,product,"RectCoordinate")
display(list1.listMat,list2.listMat,product,"PolarCoordinate")

a=print("hello")


