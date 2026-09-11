"""
======================================================================
 Program     : 002_Data_Types.py
 Topic       : Fundamentals - Data Types
 Description : Demonstrates basic Python built-in data types.
 Language    : Python
 Repository  : Python_Programming
 Author      : Samarth Antre
======================================================================
"""
print("------------------------------------------------------------------")
print("---------------------1) Numeric Data Type ------------------------")
print("------------------------------------------------------------------")

X = 11
Y = 89.90
Z = 8+6j

print("Actual Value of X is : ",X)
print("Data type of X is : ",type(X))

print("Actual Value of Y is : ",Y)
print("Data type of Y is : ",type(Y))

print("Actual Value of Z is : ",Z)
print("Data type of Z is : ",type(Z))

print("------------------------------------------------------------------")
print("----------------------2) Text Data Type --------------------------")
print("------------------------------------------------------------------")

Name = "Samarth"

print("Actual value of Name is : ",Name)
print("Data type of Name is : ",type(Name))

print("------------------------------------------------------------------")
print("----------------------3) Sequence Data Type ----------------------")
print("------------------------------------------------------------------")

Data1 = [11,21,51,101]
Data2 = (11,21,51,101)
Data3 = range(1,8,2)

print("Actual Values of Data1 is : ",Data1)
print("Data type of Data1 is : ",type(Data1))

print("Actual Values of Data2 is : ",Data2)
print("Data type of Data2 is : ",type(Data2))

print("Actual Values of Data3 is : ",Data3)
print("Data type of Data3 is : ",type(Data3))
print("Sequence of given data will be ",list(Data3))

print("------------------------------------------------------------------")
print("------------------------4) Set Data Type -------------------------")
print("------------------------------------------------------------------")

Marks = {78,92,75,65}

print("Actual Values of Marks is : ",Marks)
print("Data type of Marks is : ",type(Marks))

print("------------------------------------------------------------------")
print("------------------------5) Mapping Data Type ---------------------")
print("------------------------------------------------------------------")

Students = {"Name" : "Samarth","Age" : 23,"Marks" : 85}

print("Actual Values of Student is : ",Students)
print("Data type of Students is : ",type(Students))

print("------------------------------------------------------------------")
print("------------------------6) Binary Data Type-----------------------")
print("------------------------------------------------------------------")

B1 = b"Hello"
B2 = bytearray(b"Hello")

print("Actual value of B1 is : ",B1)
print("Data type of B1 is : ",type(B1))

print("Actual value of B2 is : ",B2)
print("Data type of B2 is : ",type(B2))

print("------------------------------------------------------------------")
print("------------------------7) None Data Type-------------------------")
print("------------------------------------------------------------------")

Result = None

print("Actual value in Result is : ",Result)
print("Data type of Result is : ",type(Result))

print("------------------------------------------------------------------")
print("------------------------8) Boolean Data Type----------------------")
print("------------------------------------------------------------------")

Flag1 = True
Flag2 = False

print("Actual value of Flag1 is : ",Flag1)
print("Data type of Flag1 is : ",type(Flag1))

print("Actual value of Flag2 is : ",Flag2)
print("Data type of Flag2 is : ",type(Flag2))

print("------------------------------------------------------------------")









