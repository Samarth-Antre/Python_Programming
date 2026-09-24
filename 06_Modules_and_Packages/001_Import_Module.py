"""
======================================================================
 Program     : 002_Import_Module.py
 Topic       : Modules - Importing a Module
 Description : Demonstrates importing a user-defined module and
               calling a function from that module.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

import Marvellous
# import Marvellous as MI
# from Marvellous import Addition,Substraction
# from Marvellous import *

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Marvellous.Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Marvellous.Substraction(Value1, Value2)
    print("Substraction is : ", Ret)

if __name__ == "__main__":
    main()