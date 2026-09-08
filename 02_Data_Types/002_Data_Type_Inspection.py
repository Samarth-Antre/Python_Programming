"""
======================================================================
 Program     : 003_Data_Type_Functions.py
 Topic       : Fundamentals - Data Type Functions
 Description : Demonstrates type(), id(), sys.getsizeof(), and len()
               functions in Python.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""
import sys
#---------------------------------------------------------------------
# Numeric Type
#---------------------------------------------------------------------
print("---------------------1) Numeric Data Type ---------------------")
X = 11
Y = 89.90
Z = 8+6j

print(X)
print(type(X))
print(id(X))
print(sys.getsizeof(X))

print(Y)
print(type(Y))
print(id(Y))
print(sys.getsizeof(Y))

print(Z)
print(type(Z))
print(id(Z))
print(sys.getsizeof(Z))

#---------------------------------------------------------------------
# Text Type
#---------------------------------------------------------------------
print("----------------------2) Text Data Type --------------------------")

Name = "Samarth"

print(Name)
print(type(Name))
print(id(Name))
print(sys.getsizeof(Name))
print(len(Name))

#---------------------------------------------------------------------
# Sequence Type
#---------------------------------------------------------------------
print("----------------------3) Sequence Data Type ----------------------")

Data1 = [11,21,51,101]
Data2 = (11,21,51,101)
Data3 = range(1,8,2)
#       range(start,End,Step)  

print(Data1)
print(type(Data1))
print(id(Data1))
print(sys.getsizeof(Data1))
print(len(Data1))

print(Data2)
print(type(Data2))
print(id(Data2))
print(sys.getsizeof(Data2))
print(len(Data2))

print(Data3)
print(type(Data3))
print(list(Data3))
print(id(Data3))
print(sys.getsizeof(Data3))
print(len(Data3))

#-------------------------------------------------------------------------
# Set Type
#-------------------------------------------------------------------------
print("------------------------4) Set Data Type -------------------------")

Marks = {78,92,75,65}

print(Marks)
print(type(Marks))
print(id(Marks))
print(sys.getsizeof(Marks))
print(len(Marks))

#------------------------------------------------------------------------
# Mapping Type
#------------------------------------------------------------------------
print("------------------------5) Mapping Data Type ---------------------")

Students = {"Name" : "Samarth","Age" : 23,"Marks" : 85}

print(Students)
print(type(Students))
print(id(Students))
print(sys.getsizeof(Students))
print(len(Students))

#------------------------------------------------------------------------
# Binary Type
#------------------------------------------------------------------------
print("------------------------6) Binary Data Type-----------------------")

B1 = b"Hello"
B2 = bytearray(b"Hello")

print(B1)
print(type(B1))
print(id(B1))
print(sys.getsizeof(B1))
print(len(B1))

print(B2)
print(type(B2))
print(id(B2))
print(sys.getsizeof(B2))
print(len(B2))

#------------------------------------------------------------------------
# None Type
#------------------------------------------------------------------------
print("------------------------7) None Data Type-----------------------")

Result = None

print(Result)
print(type(Result))
print(id(Result))
print(sys.getsizeof(Result))

#------------------------------------------------------------------------
# Boolean Type
#------------------------------------------------------------------------
print("------------------------8) Boolean Data Type-----------------------")

Flag1 = True
Flag2 = False

print(Flag1)
print(type(Flag1))
print(id(Flag1))
print(sys.getsizeof(Flag1))

print(Flag2)
print(type(Flag2))
print(id(Flag2))
print(sys.getsizeof(Flag2))




