"""
======================================================================
 Program     : 008_List_Summation_Using_Function.py
 Topic       : Lists - Summation Using a Function
 Description : Demonstrates calculating the sum of list elements
               using a user-defined function and a for loop.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def Summation(Data):

    Sum = 0
    for no in Data:
        Sum = Sum + no

    return Sum

def main():

    Marks = [78, 90, 56, 98, 77]

    Ret = Summation(Marks)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()