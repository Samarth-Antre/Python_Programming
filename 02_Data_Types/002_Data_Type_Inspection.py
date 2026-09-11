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
print("------------------------------------------------------------------")
print("---------------------1) Numeric Data Type ------------------------")
print("------------------------------------------------------------------")

X = 11
Y = 89.90
Z = 8+6j

print("Actual data : ",X)
print("Data Type : ",type(X))
print("Memory Address : ",id(X))
print("Memory Size : ",sys.getsizeof(X))

print("Actual data : ",Y)
print("Data Type : ",type(Y))
print("Memory Address : ",id(Y))
print("Memory Size : ",sys.getsizeof(Y))

print("Actual data : ",Z)
print("Data Type : ",type(Z))
print("Memory Address : ",id(Z))
print("Memory Size : ",sys.getsizeof(Z))

print("------------------------------------------------------------------")
print("----------------------2) Text Data Type --------------------------")
print("------------------------------------------------------------------")

Name = "Samarth"

print("Actual data : ",Name)
print("Data Type : ",type(Name))
print("Memory Address : ",id(Name))
print("Memory Size : ",sys.getsizeof(Name))
print("Length : ",len(Name))

print("------------------------------------------------------------------")
print("----------------------3) Sequence Data Type ----------------------")
print("------------------------------------------------------------------")

Data1 = [11,21,51,101]
Data2 = (11,21,51,101)
Data3 = range(1,8,2)

print("Actual data : ",Data1)
print("Data Type : ",type(Data1))
print("Memory Address : ",id(Data1))
print("Memory Size : ",sys.getsizeof(Data1))
print("Length : ",len(Data1))

print("Actual data : ",Data2)
print("Data Type : ",type(Data2))
print("Memory Address : ",id(Data2))
print("Memory Size : ",sys.getsizeof(Data2))
print("Length : ",len(Data2))

print("Actual data : ",Data3)
print("Data Type : ",type(Data3))
print("Sequence : ",list(Data3))
print("Memory Address : ",id(Data3))
print("Memory Size : ",sys.getsizeof(Data3))
print("Length : ",len(Data3))

print("------------------------------------------------------------------")
print("------------------------4) Set Data Type -------------------------")
print("------------------------------------------------------------------")

Marks = {78,92,75,65}

print("Actual data : ",Marks)
print("Data Type : ",type(Marks))
print("Memory Address : ",id(Marks))
print("Memory Size : ",sys.getsizeof(Marks))
print("Length : ",len(Marks))

print("------------------------------------------------------------------")
print("------------------------5) Mapping Data Type ---------------------")
print("------------------------------------------------------------------")

Students = {"Name" : "Samarth","Age" : 23,"Marks" : 85}

print("Actual data : ",Students)
print("Data Type : ",type(Students))
print("Memory Address : ",id(Students))
print("Memory Size : ",sys.getsizeof(Students))
print("Length : ",len(Students))

print("------------------------------------------------------------------")
print("------------------------6) Binary Data Type-----------------------")
print("------------------------------------------------------------------")

B1 = b"Hello"
B2 = bytearray(b"Hello")

print("Actual data : ",B1)
print("Data Type : ",type(B1))
print("Memory Address : ",id(B1))
print("Memory Size : ",sys.getsizeof(B1))
print("Length : ",len(B1))

print("Actual data : ",B2)
print("Data Type : ",type(B2))
print("Memory Address : ",id(B2))
print("Memory Size : ",sys.getsizeof(B2))
print("Length : ",len(B2))

print("------------------------------------------------------------------")
print("------------------------7) None Data Type-------------------------")
print("------------------------------------------------------------------")

Result = None

print("Actual data : ",Result)
print("Data Type : ",type(Result))
print("Memory Address : ",id(Result))
print("Memory Size : ",sys.getsizeof(Result))

print("-------------------------------------------------------------------")
print("------------------------8) Boolean Data Type-----------------------")
print("------------------------------------------------------------------")

Flag1 = True
Flag2 = False

print("Actual data : ",Flag1)
print("Data Type : ",type(Flag1))
print("Memory Address : ",id(Flag1))
print("Memory Size : ",sys.getsizeof(Flag1))

print("Actual data : ",Flag2)
print("Data Type : ",type(Flag2))
print("Memory Address : ",id(Flag2))
print("Memory Size : ",sys.getsizeof(Flag2))

print("------------------------------------------------------------------")





