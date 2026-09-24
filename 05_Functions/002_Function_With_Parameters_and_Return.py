"""
======================================================================
 Program     : 002_Function_With_Parameters_and_Return.py
 Topic       : Functions - Parameters and Return Value
 Description : Demonstrates passing parameters to a function and
               returning the result.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans


def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)

    print("Addition is : ", Ret)


if __name__ == "__main__":
    main()