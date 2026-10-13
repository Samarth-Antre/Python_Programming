"""
======================================================================
 Program     : 009_Modifying_Global_Variable_Using_Global_Keyword.py
 Topic       : Functions - Modifying a Global Variable
 Description : Demonstrates modifying a global variable inside a
               function using the global keyword.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

no = 11

def Display():
    global no
    no = 21
    print("From Display : ", no)

print("Before : ", no)
Display()
print("After : ", no)