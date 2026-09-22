"""
======================================================================
 Program     : 003_Main_Function_and_Entry_Point.py
 Topic       : Fundamentals - Main Function and Entry Point
 Description : Demonstrates defining a main() function and using
               the __name__ == "__main__" entry-point check.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():
    print("Inside main")
    print(__name__)

if __name__ == "__main__":
    main()