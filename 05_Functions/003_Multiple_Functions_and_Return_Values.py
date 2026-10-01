"""
======================================================================
 Program     : 003_Multiple_Functions_and_Return_Values.py
 Topic       : Functions - Multiple Functions and Return Values
 Description : Demonstrates multiple functions with parameters and
               return values, including multiple return values.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

# --------------------------------------------------------------------
# 1) Multiple Functions with Return Values
# --------------------------------------------------------------------

def Multiplication(No1, No2):
    return No1 * No2

def Division(No1, No2):
    return No1 / No2

# --------------------------------------------------------------------
# 2) Multiple Return Values
# --------------------------------------------------------------------

def Calculation(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mult = No1 * No2
    Div = No1 / No2

    return Add, Sub, Mult, Div

def main():

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    print("\n-------------------- Multiple Functions -----------------------")

    Ret1 = Multiplication(Value1, Value2)
    print("Multiplication is : ", Ret1)

    Ret2 = Division(Value1, Value2)
    print("Division is : ", Ret2)

    print("\n----------- Single Function - Multiple Return Values -------------")

    Ret1, Ret2, Ret3, Ret4 = Calculation(Value1, Value2)

    print("Addition is : ", Ret1)
    print("Subtraction is : ", Ret2)
    print("Multiplication is : ", Ret3)
    print("Division is : ", Ret4)

if __name__ == "__main__":
    main()