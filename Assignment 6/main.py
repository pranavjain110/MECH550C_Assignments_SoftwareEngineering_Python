'''
___________________________________________________________________________
Date: March 9, 2020
Student Number = 14213029
Source File: main.py

Course: MECH 550C - Software Design
Assignment Number: 6

Purpose: Demonstrating Various Data Collections

Description:
This code demonstrates the use of of the following types of collections
-List
-Queue
-Stack
-LinkedList
-Dictionary

The program stores an instance of the class in each of the above mentioned
data collections and then retrieves one of the entries.

Usage: Run main.exe
__________________________________________________________________________
'''

from queue import Queue, LifoQueue


class weights1D():
    """Class used to store values attached to a given node

    """
    def __init__(self, nodeX, nodeNumber):
        """Constructor to initialize a 1D node

        Arguments:
            nodeX {float} -- value corresponsing to a node
            nodeNumber {int} -- name of the node
        """
        self.nodeX = nodeX
        self.nodeNumber = nodeNumber

    def __str__(self):
        """method overloading to print object of class

        Returns:
            string -- string to be printed
        """
        a = "Node Number ({}): ".format(self.nodeNumber)
        if hasattr(self, 'nodeX'):
            a += "Node N(X): {} |".format(self.nodeX)
        if hasattr(self, 'nodeY'):
            a += "Node N(Y): {} |".format(self.nodeY)
        if hasattr(self, 'nodeZ'):
            a += "Node N(Z): {}|".format(self.nodeZ)
        return a


class weights2D(weights1D):
    """Child class capable of storing 2 node value

    """
    def __init__(self, nodeX, nodeY, nodeNumber):
        """Constructor to initialize a 2D node

        Arguments:
            nodeX {float} -- value corresponsing to a node
            nodeY {float} -- value corresponsing to a node
            nodeNumber {int} -- name of the node
        """
        super().__init__(nodeX, nodeNumber)
        self.nodeY = nodeY


class weights3D(weights2D):
    """Child class capable of storing 3 node value

    """
    def __init__(self, nodeX, nodeY, nodeZ, nodeNumber):
        """Constructor to initialize a 3D node

        Arguments:
            nodeX {float} -- value corresponsing to a node
            nodeY {float} -- value corresponsing to a node
            nodeZ {int} -- value corresponsing to a node
            nodeNumber {int} -- name of the node
        """
        super().__init__(nodeX, nodeY, nodeNumber)
        self.nodeZ = nodeZ


#____________________________________________________________________________
# 1. Storing objects in a list
a = []


# Appending instance of class weight3D to the list
a.append(weights3D(32, 40, 50, nodeNumber=1))
a.append(weights3D(22, 99, 20, nodeNumber=2))
a.append(weights3D(22, 31, 31, nodeNumber=3))

print("_"*100)
print("List Created:")
for element in a:
    print(element)
print("\nInitial size of the list = {}".format(len(a)))

# display the element at index 1
print("Attributes of object stored in a[1]:\t{}".format(a[1]))
# removing the element at index 1
a.pop(1)

print("Size of the list after removing element = {}".format(len(a)))
print("\nList after deletion of element:")
for element in a:
    print(element)
print("_"*100)


#____________________________________________________________________________
# 2. Storing objects in a queue(FIFO)
q = Queue()

# Appending instance of class weight3D to the queue
q.put(weights3D(11, 12, 13, nodeNumber=1))
q.put(weights3D(22, 23, 24, nodeNumber=2))
q.put(weights3D(33, 34, 35, nodeNumber=3))


print("\nInitial size of the queue = {}".format(q.qsize()))

# Display and remove the first element of the queue
print("Popping the first element:\t{}".format(q.get()))

print("Size of the queue after removing element = {}".format(q.qsize()))
print("_"*100)


#____________________________________________________________________________
# 3. Storing objects in a stack(LIFO)
stack = LifoQueue()

# Appending instance of class weight3D to the stack
stack.put(weights3D(11, 12, 13, nodeNumber=1))
stack.put(weights3D(22, 23, 24, nodeNumber=2))
stack.put(weights3D(33, 34, 35, nodeNumber=3))


print("\nInitial size of the stack = {}".format(stack.qsize()))

# Display and remove the last element of the stack
print("Popping the last element:\t{}".format(stack.get()))

print("Size of the stack after removing element = {}".format(q.qsize()))
print("_"*100)


#____________________________________________________________________________
# 4. Storing the objects in a link list

# Code from https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# A single node of a singly linked list


# Python program to delete a node from linked list

class Node:
    """Node Class

    """
    def __init__(self, data):
        """Constructor to initialize the node object

        """
        self.data = data
        self.next = None


class LinkedList:
    """A Linked List class with a single head node

    """

    def __init__(self):
        """Constructor to initialize head
        """
        self.head = None

    def push(self, new_data):
        """Method to insert a new node at the beginning

        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNodeNumber(self, key):
        """Given a reference to the head of a list and a key,
        delete the first occurrence of key in linked list

        """

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data.nodeNumber == key):
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data.nodeNumber == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    def printList(self):
        """Method to print the linked LinkedList
        """
        temp = self.head
        while(temp):
            print("{}" .format(temp.data))
            temp = temp.next


ll = LinkedList()
# Appending instance of class weight3D to the Linked List
ll.push(weights3D(11, 22, 33, nodeNumber=1))
ll.push(weights3D(12, 23, 34, nodeNumber=2))
ll.push(weights3D(13, 23, 35, nodeNumber=3))
ll.push(weights3D(14, 24, 36, nodeNumber=4))

print("\nCreated Linked List: ")
ll.printList()
ll.deleteNodeNumber(2)
print("\nLinked List after Deletion of Node Number 2:")
ll.printList()
print("_"*100)


#____________________________________________________________________________
# 5. Store objects in a dictionaries

dict = {}

# Appending instance of class weight2D to the dictionary
dict[12] = weights2D(11, 122, nodeNumber=12)
dict[22] = weights2D(11, 222, nodeNumber=22)
dict[13] = weights2D(24, 333, nodeNumber=13)

print("Created Dictionary")
for k, v in dict.items():
    print("key= {} \t& \tvalue = {}".format(k, v))

print("\nInitial size of the dictionary = {}".format(len(dict)))

# Removing an element(key) from the dictionary
print("Removing the element with Key = 22: and Value = {}".format(dict[22]))
dict.pop(22, None)

print("Final size of the dictionary = {}\n".format(len(dict)))
print("Dictionary after deletion of key 22")
for k, v in dict.items():
    print("key= {} \t& \tvalue = {}".format(k, v))


input("\nPress Enter to Exit")
