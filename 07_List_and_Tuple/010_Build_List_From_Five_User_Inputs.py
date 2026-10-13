"""
======================================================================
 Program     : 010_Build_List_From_Five_User_Inputs.py
 Topic       : Lists - Building a List from User Input
 Description : Demonstrates accepting five integer values from the
               user and adding them to a list using append().
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

def main():
    Marks = []
    # Marks = list()

    print("Enter 5 marks : ")

    no = int(input())
    Marks.append(no)

    no = int(input())
    Marks.append(no)

    no = int(input())
    Marks.append(no)

    no = int(input())
    Marks.append(no)

    no = int(input())
    Marks.append(no)

    print("List elements are : ", Marks)

if __name__ == "__main__":
    main()