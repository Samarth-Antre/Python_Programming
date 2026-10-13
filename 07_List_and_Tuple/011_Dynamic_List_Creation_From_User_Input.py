"""
======================================================================
 Program     : 011_Dynamic_List_Creation_From_User_Input.py
 Topic       : Lists - Dynamic List Creation from User Input
 Description : Demonstrates accepting the number of elements from
               the user and creating a list dynamically using a loop.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():

    Size = 0
    Arr = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("List elements are : ", Arr)

if __name__ == "__main__":
    main()