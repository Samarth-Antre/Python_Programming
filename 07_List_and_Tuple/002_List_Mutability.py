"""
======================================================================
 Program     : 002_List_Mutability.py
 Topic       : Lists - Mutability
 Description : Demonstrates modifying an existing element of a list.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():

    Data = [10, 20, 30, 40]

    print("Original Data : ", Data)

    Data[1] = 21

    print("Modified Data : ", Data)
    print("Modified element : ", Data[1])

if __name__ == "__main__":
    main()