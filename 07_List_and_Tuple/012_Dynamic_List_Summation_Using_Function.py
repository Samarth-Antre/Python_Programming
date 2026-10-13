"""
======================================================================
 Program     : 012_Dynamic_List_Summation_Using_Function.py
 Topic       : Lists - Dynamic List Summation Using a Function
 Description : Demonstrates creating a list dynamically from user
               input and calculating its sum using a function.
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

    Size = 0
    Arr = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = Summation(Arr)

    print("Summation is : ", Ret)

if __name__ == "__main__":
    main()