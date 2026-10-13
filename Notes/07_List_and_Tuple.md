# Lists and Tuples

## Overview

A **list** is an ordered collection that can store multiple values. A list is **mutable**, which means its elements can be changed after creation.

A **tuple** is an ordered collection that is **immutable**, which means its elements cannot be reassigned after creation.

Lists and tuples can store values of different data types.

---

## List Basics

A list is created using square brackets `[]`.

### Example

```python
Data = [10, 20, 30, 40]

print(Data)
print(type(Data))
print(len(Data))
```

### Output

```text
[10, 20, 30, 40]
<class 'list'>
4
```

- `type(Data)` identifies the object's type.
- `len(Data)` returns the number of elements.
- List indexing starts at `0`.

---

## Accessing List Elements Using Indexes

Use an index inside square brackets to access an element.

```python
Data = [10, 20, 30, 40]

print(Data[0])
print(Data[1])
print(Data[2])
print(Data[3])
```

### Output

```text
10
20
30
40
```

An index must refer to an element that exists in the list. An invalid index raises an `IndexError`.

---

## List Mutability

Lists are mutable, so an element can be changed using its index.

```python
Data = [10, 20, 30, 40]

print("Original Data : ", Data)

Data[1] = 21

print("Modified Data : ", Data)
```

### Output

```text
Original Data :  [10, 20, 30, 40]
Modified Data :  [10, 21, 30, 40]
```

The assignment `Data[1] = 21` changes the second element of the list.

---

## Tuple Basics and Indexing

A tuple is created using parentheses `()`.

```python
Data = (10, 20, 30, 40)

print("Type of Data : ", type(Data))
print("Length of Data : ", len(Data))

print(Data[0])
print(Data[1])
print(Data[2])
print(Data[3])
```

A tuple supports indexing and traversal, but its elements cannot be reassigned.

---

## Tuple Immutability

The following assignment is invalid because tuples are immutable:

```python
Data = (10, 20, 30, 40)

Data[1] = 21
```

It raises a `TypeError` similar to:

```text
TypeError: 'tuple' object does not support item assignment
```

This error is intentional in an immutability demonstration. It shows that an existing tuple element cannot be changed by assignment.

---

## List vs Tuple

| Property | List | Tuple |
|---|---|---|
| Brackets used | Square brackets `[]` | Parentheses `()` |
| Ordered | Yes | Yes |
| Supports indexing | Yes | Yes |
| Mutable | Yes | No |
| Allows duplicate values | Yes | Yes |
| Can contain mixed data types | Yes | Yes |

### Example

```python
Data1 = [10, 3.14, True, "Pune"]
Data2 = (10, 3.14, True, "Pune")

print("List  : ", Data1)
print("Tuple : ", Data2)
```

Use a list when the collection needs to be modified. Use a tuple when the collection should remain fixed.

---

## List Traversal

**Traversal** means visiting the elements of a collection one at a time.

### 1. Direct Traversal

```python
Data = [11, 21, 51, 101]

for no in Data:
    print(no)
```

This approach gives each element directly.

### 2. Index-Based Traversal

```python
Data = [11, 21, 51, 101]

for i in range(len(Data)):
    print(Data[i])
```

This approach uses an index to access each element.

Both approaches are demonstrated in `006_List_Traversal.py`.

---

## Creating a List with `append()`

The `append()` method adds one element to the end of a list.

```python
Marks = []

Marks.append(11)
Marks.append(21)
Marks.append(51)
Marks.append(101)

print("List elements are : ", Marks)
```

### Output

```text
List elements are :  [11, 21, 51, 101]
```

An empty list can be created using either `[]` or `list()`.

```python
Data1 = []
Data2 = list()
```

Both statements create an empty list.

---

## Building a List from a Fixed Number of User Inputs

The `input()` function returns a string by default. Use `int()` when an integer is required.

The following example follows the fixed five-input approach used in the  program:

```python
Marks = []

print("Enter 5 marks : ")

for i in range(5):
    no = int(input())
    Marks.append(no)

print("List elements are : ", Marks)
```

---

## Dynamic List Creation from User Input

A list can be built based on the number of elements entered by the user.

```python
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
```

### Example

```text
Enter the number of elements :
4
Enter the elements :
11
21
51
101
List elements are :  [11, 21, 51, 101]
```

Here, `Size` determines how many elements are collected. `range(Size)` repeats the input operation that many times.

---

## List Summation Using a Loop

An **accumulator** is a variable that stores a running result. To calculate a sum, initialize it to `0` and add each element.

```python
Marks = [78, 90, 56, 98, 77]

Sum = 0

for no in Marks:
    Sum = Sum + no

print("Addition is : ", Sum)
```

### Output

```text
Addition is :  399
```

The variable `Sum` is updated each time the loop processes an element.

---

## List Summation Using a Function

A function can receive a list as an argument, calculate the sum, and return the result.

```python
def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum


def main():
    Marks = [78, 90, 56, 98, 77]

    Ret = Summation(Marks)

    print("Addition is : ", Ret)


if __name__ == "__main__":
    main()
```

The function can be reused with different lists. This example adds function arguments and return values to the list-summation concept.

---

## Dynamic List Summation Using a Function

This example combines dynamic list creation with function-based summation.

```python
def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum


def main():
    Arr = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = Summation(Arr)
    print("Summation is : ", Ret)


if __name__ == "__main__":
    main()
```

This example brings together:

- List creation.
- User input and integer conversion.
- `for` loop and `range()`.
- `append()`.
- Passing a list to a function.
- Accumulator and `return`.

---

## Important Points

- Lists use `[]`; tuples commonly use `()`.
- List and tuple elements can be accessed using indexes.
- Indexing starts at `0`.
- `len()` returns the number of elements.
- Lists are mutable; tuples are immutable.
- `for element in Data` performs direct traversal.
- `range(len(Data))` can be used for index-based traversal.
- `append()` adds one element to the end of a list.
- `input()` returns a string by default.
- `int(input())` converts numeric input to an integer.
- An accumulator stores a running result such as a sum.
- A function can accept a list and return a calculated value.
- A tuple item-assignment attempt raises a `TypeError`.

---

## Quick Revision

- **List** → Ordered, mutable collection.
- **Tuple** → Ordered, immutable collection.
- **Index** → Position used to access an element; starts at `0`.
- **`len(Data)`** → Number of elements.
- **`Data[index] = value`** → Changes a list element.
- **`for no in Data`** → Direct traversal.
- **`range(len(Data))`** → Index-based traversal.
- **`append(value)`** → Adds an element to a list.
- **`[]` / `list()`** → Create an empty list.
- **Accumulator** → Stores a running result.
- **`return`** → Sends a function's result back to the caller.
- **Tuple item assignment** → Raises `TypeError`.

---


