"""
======================================================================
 Program     : 004_Nested_Functions.py
 Topic       : Functions - Nested Functions
 Description : Demonstrates defining a function inside another
               function and calling the nested function from within
               the outer function.
 Language     : Python
 Repository   : Python_Programming
 Author       : Samarth Antre
======================================================================
"""

def BigBazar():

    print("------------- Nested Function Definition -------------")
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlor")

    # Amul() can be accessed inside BigBazar.

def BigBazarX():

    print("\n------------- Nested Function Call -------------------")
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream parlor")

    Amul()
    Amul()

def main():

    BigBazar()
    BigBazarX()

if __name__ == "__main__":
    main()