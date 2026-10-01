"""
======================================================================
 Program     : 005_Types_of_Parameters.py
 Topic       : Functions - Types of Parameters
 Description : Demonstrates positional, keyword, default and
               variable-length parameters.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

# --------------------------------------------------------------------
# 1 & 2) Positional and Keyword Parameters
# --------------------------------------------------------------------

def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

# --------------------------------------------------------------------
# 3) Default Parameter
# --------------------------------------------------------------------

def AreaD(Radius, PI=7.12):
    Ans = PI * Radius * Radius
    return Ans

# --------------------------------------------------------------------
# 4) Variable-Length Parameter
# --------------------------------------------------------------------

def Display(*Data):
    print(Data)
    print("Type of parameter is : ", type(Data))

def main():

    print("---------- Positional Parameter ----------")

    Ret = Area(10.5, 3.14)
    print("Area of circle is : ", Ret)

    print("\n---------- Keyword Parameter -------------")

    Ret = Area(Radius=10.5, PI=3.14)
    print("Area of circle is : ", Ret)

    print("\n---------- Default Parameter -------------")

    Ret = AreaD(10.5)
    print("Area of circle is : ", Ret)

    print("\n---------- Variable-Length Parameter -----")

    Display(10, 45, 52.2, "Samarth", False)

if __name__ == "__main__":
    main()