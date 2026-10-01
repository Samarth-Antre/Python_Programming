"""
======================================================================
 Program     : 004_Tuple_Immutability.py
 Topic       : Tuples - Immutability
 Description : Demonstrates that an existing element of a tuple
               cannot be modified.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():

    Data = (10, 20, 30, 40)

    print("Original Data : ", Data)

    Data[1] = 21

    print("Modified Data : ", Data)

if __name__ == "__main__":
    main()