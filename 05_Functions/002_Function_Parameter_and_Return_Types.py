"""
======================================================================
 Program     : 002_Function_Parameter_and_Return_Types.py
 Topic       : Functions - Parameters and Return Values
 Description : Demonstrates functions with different combinations of
               parameters and return values.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

# --------------------------------------------------------------------
# 1) No Parameter and No Return Value
# --------------------------------------------------------------------

def Marvellous1():
    print("Inside Marvellous")

# --------------------------------------------------------------------
# 2) One Parameter and No Return Value
# --------------------------------------------------------------------

def Marvellous2(Value):
    print("Inside Marvellous : ", Value)

# --------------------------------------------------------------------
# 3) One Parameter and One Return Value
# --------------------------------------------------------------------

def Marvellous3(Value):
    print("Inside Marvellous : ", Value)
    return 21

# --------------------------------------------------------------------
# 4) Multiple Parameters and One Return Value
# --------------------------------------------------------------------

def Marvellous4(Value1, Value2):
    print("Inside Marvellous : ", Value1, Value2)
    return 21

# --------------------------------------------------------------------
# 5) Multiple Parameters and Multiple Return Values
# --------------------------------------------------------------------

def Marvellous5(Value1, Value2):
    print("Inside Marvellous : ", Value1, Value2)
    return 21, 51

def main():

    print("------------- 1) No Parameter, No Return -------------------")

    Marvellous1()

    print("\n------------- 2) One Parameter, No Return ----------------")

    Marvellous2(11)

    print("\n------------- 3) One Parameter, One Return ---------------")

    Ret = Marvellous3(11)
    print("Return value is : ", Ret)

    print("\n------------- 4) Multiple Parameters, One Return ---------")

    Ret = Marvellous4(10, 20)
    print("Return value is : ", Ret)

    print("\n------------- 5) Multiple Parameters, Multiple Return ----")
    
    Ret1, Ret2 = Marvellous5(10, 20)
    print("Return values are : ", Ret1, Ret2)

if __name__ == "__main__":
    main()







