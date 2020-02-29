'''
________________________________________________________________________
Date: February 12, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Asignment Number: 4

Purpose: Multiply two matrices with complex numbers

Description: This code demonstrates the concepts of Classes and Function 
Overloading to multiply and display complex numbers.
The program takes in two lists containing  tuples representing a complex 
number,  stores each  element as  an object of class  ComplexNumbers and 
returns a product of two  matrices as a list, whose each element is also 
an object of class ComplexNumbers.

Usage: Run main.exe
________________________________________________________________________
'''

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
    
    def __str__(self):
        """Method overloading to print a complex number in a+bi string format 
        
        Returns:
           string -- string containg complex number in a+bi format
        """
        output=""
        if self.read()[0] > 0:
            sign1st = ""
        elif self.read()[0] == 0:
            sign1st = ""
        else:
            sign1st = "-"

        if self.read()[1] > 0:
            sign2nd = "+"
        elif self.read()[1] == 0 or self.read()[0] == 0 :
            sign2nd = ""
        else:
            sign2nd = "-"
        readFuncType = self.read 

        
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
            arg1="0"

            
        output += "{0}{1}{2}{3}{4}".format(sign1st,arg1,sign2nd,arg2,imSym)
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
            {tuple} -- tuple containg Absolute value and phase of a polar number
        """
        absValue= math.sqrt((self.__r**2)+(self.__i**2))
        phase = math.atan2(self.__i,self.__r)
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
        """This method is used to subtact 2 complex numbers input as an object of class ComplexNumbers

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
    """This matrix is used to store each variable of a list containg tuples, representing elements of a matrix as an object of class ComplexNumbers and Carry out the multiplication of 2 matrices
    
    Returns:
        {list} -- each element of the list is an object of class ComplexNumbers
    """
    
    def __init__(self,listOfElements,row,col):

        # Condition to check if dimention of matrices are entered as integers
        if not (isinstance(row, int) and isinstance(col, int) ):
            print(
                "\n\nPlease ensure that the dimension of the Matrices are integers\n\n")
            quit()

        # Condition to check the dimensions of matrices entered are positive
        if row < 1 or col < 1 :
            print("\n\nNumber of rows or columns cannot be less than 1\n\n")
            quit()


        # Conditions to ensure that the number of elements
        # in a matrix match the product of its row and column
        if len(listOfElements) != row*col:
            print("\n\nEnsure that the number of elements entered in matrix 1 are equal " +
                  "to the product of specified number of rows and columns of the matrix.\n\n")
            quit()


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
        # Condition to check if the matries can be multplied
        if self.col != mat2.row:
            print("\n\nIncorrect dimensions for matrix multiplication. Ensure that the number of " +
                  "columns in the first matrix matches the number of rows in the second matrix.\n")
            quit()

        # creates and empty 2d list with each of its element being a tuple
        self.result = [[ComplexNumbers(0, 0) for i in range(mat2.col)] for j in range(self.row)]

        # logic to multiply two matrices
        for i in range(0, self.row):
            for j in range(0, mat2.col):
                for k in range(0, self.col):
                    self.result[i][j] = self.result[i][j] + (self.listMat[i][k] *  mat2.listMat[k][j])
        return self.result


# Function to form a string to display Complex Matrices
def displayComplexMatrix(matrixToDisplay):
    """This method takes in a list of tuples representing a matix and converts it into a string

    Arguments:
        matrixToDisplay {list} -- list containing all the elements of a matrix as object of class ComplexNumbers

    Returns:
        strOutput -- input matrix conveted to a string
    """

    strOutput = ""
    for i in range(len(matrixToDisplay)):
        for j in range(len(matrixToDisplay[0])):
            
                strOutput += (str(matrixToDisplay[i][j])).ljust(20)
        strOutput = strOutput + "\n"
    return strOutput


#Function to display matrices and their product
def display(mat1, mat2, resultMat):
    """This functions is used to print the two matrices to be multiplied and their product

    Arguments:
        mat1 {list} -- list containing the 1st matrix
        mat2 {lsit} -- list containing the 2nd matrix
        resultMat {list} -- list containing the product of matrices
    """
             
    print("\n1st Matrix is: ")
    print(displayComplexMatrix(mat1))
    print("2nd Matrix is: ")
    print(displayComplexMatrix(mat2))
    print("Product of the matrices is:")
    print(displayComplexMatrix(product))
    print("__________________________________________")




# -----------------------Main Program Starts Here---------------------------------

# Displaying matrices and their product (for assignment 4)
# represents rows and columns of the first and the second matrix to be multiplied
row1, col1 = 2, 2
row2, col2 = 2, 2

# listA and listB represent the elements of the 1st and 2nd matrix to be multiplied
listA = [(1, 1), (2, 0), (0, 0), (2, 5)]
listB = [(5, -5), (0, -2), (0, 4.2), (-11.1, 0)]

list1=ComplexMultiplication(listA,row1,col1)
list2=ComplexMultiplication(listB,row2,col2)
product=list1.multiplyMat(list2)
print("_____________________________")
display(list1.listMat,list2.listMat,product)



# Function used to test the outputs of the overloaded method __str__ (for assignment 4)
def printComplexNum(number):
    num=ComplexNumbers(number[0],number[1])
    print("{0}\tis  {1}".format(number,num))

numArray=[(3,5),(3,-5),(0,5),(0,-5),(3,0),(0,0),(-7,0)]
print("\nPrinting Complex Numbers in a nice string:")
for number in numArray:
    printComplexNum(number)


# Function used to test the outputs of the method that returns polar number(for assignment 4)
print("_______________________________________________________________")
def printPolarNum(number):
    num=ComplexNumbers(number[0],number[1])
    polarNum=num.returnPolar()
    print("{0} \tis : Absolute Value = {1:.3f} \tand \tPhase = {2:.3f} rad".format(num,polarNum[0],polarNum[1]))

print("\nPolar form of: ")
numArray=[(10,2),(10,-2),(0,-2),(-2,0),(6,-8)]
for number in numArray:
    printPolarNum(number)

# Display addition and subtraction operator overloading
a = ComplexNumbers(2, 3)
b = ComplexNumbers(-5, 3)
print("_________________________________________________")
print("\nThe sum of {}  and  {} is:  {}".format(a,b,a+b))
print("The difference of {}  and  {} is:  {}".format(a,b,a-b))

# Taking input from the user to exit the program
input("\n\nPlease press the Enter key to exit.\n")