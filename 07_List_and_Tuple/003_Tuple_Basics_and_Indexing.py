"""
======================================================================
 Program     : 003_Tuple_Basics_and_Indexing.py
 Topic       : Tuples - Basics and Indexing
 Description : Demonstrates creating a tuple, checking its type and
               length, and accessing elements using indexes.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():

    Data = (10, 20, 30, 40)

    print("Type of Data : ", type(Data))
    print("Length of Data : ", len(Data))

    print("First element : ", Data[0])
    print("Second element : ", Data[1])
    print("Third element : ", Data[2])
    print("Fourth element : ", Data[3])

if __name__ == "__main__":
    main()