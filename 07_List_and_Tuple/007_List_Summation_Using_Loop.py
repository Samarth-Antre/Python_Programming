"""
======================================================================
 Program     : 007_List_Summation_Using_Loop.py
 Topic       : Lists - Summation Using a Loop
 Description : Demonstrates calculating the sum of all elements in a
               list using a for loop and an accumulator variable.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():

    Marks = [78, 90, 56, 98, 77]

    Sum = 0
    for no in Marks:
        Sum = Sum + no

    print("Addition is : ", Sum)

if __name__ == "__main__":
    main()