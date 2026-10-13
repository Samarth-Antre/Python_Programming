"""
======================================================================
 Program     : 006_Global_Variable_Access.py
 Topic       : Functions - Global Variable Access
 Description : Demonstrates accessing a global variable from multiple
               user-defined functions.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

no = 11     # Global variable

def Display():
    print("From display : ", no)

def Demo():
    print("From demo : ", no)

if __name__ == "__main__":
    Display()
    Demo()