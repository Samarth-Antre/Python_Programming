"""
======================================================================
 Program     : 005_List_vs_Tuple.py
 Topic       : Lists and Tuples - Comparison
 Description : Demonstrates common properties of lists and tuples,
               including ordering, indexing, mutability and
               heterogeneous data.
 Language     : Python
 Repository   : Python_Programming
 Author       : Samarth Antre
======================================================================
"""

# --------------------------------------------------------------------
# List and Tuple Properties
# --------------------------------------------------------------------

#                    List    Tuple
# Ordered             Yes     Yes
# Indexed             Yes     Yes
# Mutable             Yes     No
# Heterogeneous       Yes     Yes


def main():

    Data1 = [10, 3.14, True, "Pune"]    # heterogeneous data
    Data2 = (10, 3.14, True, "Pune")

    print("List  : ", Data1)
    print("Tuple : ", Data2)

    print("\nList first element  : ", Data1[0])
    print("Tuple first element : ", Data2[0])

    print("\n------------- List is Mutable -------------")

    Data1[1] = 11
    print("Modified List : ", Data1)

    print("\n------------- Tuple is Immutable ----------")

    # Data2[1] = 11       # Error
    # print(Data2)


if __name__ == "__main__":
    main()