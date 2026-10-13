"""
======================================================================
 Program     : 007_Local_Variable_Scope_Expected_NameError.py
 Topic       : Functions - Local Variable Scope
 Description : Demonstrates that a local variable defined inside one
               function cannot be accessed directly from another
               function.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

no = 11     # Global variable

def Display():
    
    a = 21   # Local variable

    print("From display : ", no)
    print("From display value of a is : ", a)

def Demo():
    print("From demo value of a is : ", a)
    print("From demo : ", no)

if __name__=="__main__":
    Display()
    Demo()
