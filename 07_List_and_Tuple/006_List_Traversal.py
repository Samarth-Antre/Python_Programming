"""
======================================================================
 Program     : 006_List_Traversal.py
 Topic       : Lists - Traversal
 Description : Demonstrates accessing list elements using a for loop
               and using indexes with range().
 Language     : Python
 Repository  : Python_Programming
 Author       : Samarth Antre
======================================================================
"""

def main():

    Marks = [78, 90, 45, 65]

    print("------------- Direct Traversal -------------")

    for no in Marks:
        print(no)

    print("\n------------- Index Based Traversal --------")

    for i in range(len(Marks)):
        print(Marks[i])

if __name__ == "__main__":
    main()