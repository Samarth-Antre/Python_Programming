
"""
======================================================================
 Program     : 001_Procedural_Style_Addition.py
 Topic       : Programming Styles - Procedural Style
 Description : Demonstrates performing addition using a
               user-defined function in procedural programming.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans


def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Addition(Value1, Value2)

    print("Addition is : ", Ret)


if __name__ == "__main__":
    main()
