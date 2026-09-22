"""
======================================================================
 Program     : 001_Selection.py
 Topic       : Control Statements - Selection
 Description : Demonstrates selection using if, elif, and else.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""

print("========================================")
print("       Ticket Pricing Software")
print("========================================")

print("Please enter your age : ")
Age = int(input())

if Age <= 5:
    print("Free entry")
elif Age <= 18:
    print("Ticket price : 900")
elif Age <= 40:
    print("Ticket price : 1200")
else:
    print("Ticket price : 500")