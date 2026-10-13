"""
======================================================================
 Program     : 008_Local_Variable_Shadowing_Global.py
 Topic       : Functions - Local Variable Shadowing Global
 Description : Demonstrates how a local variable with the same name
               as a global variable behaves inside a function.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

no = 11

def Display():
    no = 21
    print("From Display : ", no)

print("Before : ", no)
Display()
print("After : ", no)


    