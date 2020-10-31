# Assignment 6- MECH550C

---
Title: Demonstrating Various Data Collections

Author: Pranav Jain

Student Number: 14213029

Date: 9 March, 2020

---

## Description

This code demonstrates the use of of the following types of collections

- List
- Queue
- Stack
- LinkedList
- Dictionary

The program stores an instance of the class in the collections mentioned above.

**main.exe** file is the compiled program which the demonstrates the addition of data to the collections and then retrieving one of the entries

### Use of each collection

#### List

Would be useful in an application which requires us to calculate the center of gravity of an object and thus the position of all the nodes would be required.

#### Queue

Could be useful in calculation of the frame angles in Robotics. Node X,Y and Z could represent the rotations about the Current frame. Since the current frame angles are post-multiplied, hence the values that are entered first must be multiplied first (FIFO).  

#### Stack

Could be useful in calculation of the frame angles in Robotics. Node X,Y and Z could represent the rotations about the Origin frame. Since the current frame angles are pre-multiplied, hence the values that are entered last must be multiplied first (LIFO).

#### Linked List

Linked list would function like a list, but it would have a efficient memory utilization. Linked list also has a Faster Access time,can be expanded in constant time without memory overhead.

#### Dictionary

Useful in application where you would need to find the center of gravity of the given points mentioned by the frame number stored as key. Since each frame is unique, it is stored as a key.

## Execution

Run **main.exe** to see the output of the the program

The following command was used to form the executable file

```bash
pyinstaller main.py --onefile
```

## Dependencies

- Python 3.7.5 64-bit
- Python Standard Libraries
  - queue — A synchronized queue class
- pyInstaller is used to convert the following code into .exe file
- OS: Windows 10 64-bit

## IDE

- Visual Studio Code
