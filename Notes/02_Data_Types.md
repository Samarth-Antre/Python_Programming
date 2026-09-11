# Data Types in Python

## Overview

A **data type** defines the type of a value and the set of operations that can be performed on that value.

A data type specifies:

- The kind of data a variable can store.
- The operations that can be performed on it.
- The memory size required to store it.

In Python, everything is an **object**, and every object belongs to some class or data type.

Every object has:

- A value
- A data type
- A memory address

---

## Python is a Dynamically Typed Language

Python is a **dynamically typed language**.

- Data type does not need to be declared before creating a variable.
- The type is automatically assigned during runtime based on the value assigned.
- The type of a variable can change by assigning a new value of a different type.
- Type safety is ensured during execution.

### Example

```python
x = 11
print(type(x))

x = "Jay Ganesh..."
print(type(x))
```

Variables are just **labels pointing to objects**, and the object carries the type information, not the variable itself.

---

## Static Typing

C, C++, and Java are examples of **statically typed languages**.

- Data type must be declared before execution.
- Variable follows its declared type.
- Type checking occurs at compile time.

### Example

```java
int x = 11;
```

---

## Dynamic Typing vs Static Typing

| Dynamic Typing | Static Typing |
|----------------|---------------|
| Python | C, C++, Java |
| Type is determined at runtime | Type is checked at compile time |
| No mandatory type declaration | Data type is declared |
| Variable can refer to objects of different types | Variable follows its declared type |

---

## Variable Creation in Python

A variable is a name that refers to a location in memory where data is stored.

It acts as a **reference** to an object.

### Example

```python
a = 11
```

Internally:

1. Object `11` is created in heap memory.
2. Data type `int` is attached to the object.
3. Variable `a` points to that object.

> A variable is a reference, not a container.

---

# Built-in Data Types

Python provides several built-in data types.

## Numeric Data Types

### int (Integer)

The `int` data type is used to store whole numbers without a decimal point.

- Stores whole numbers.
- Can be positive, negative, or zero.
- Integer size can grow depending on available memory.

### Example

```python
x = 11

print(x)
print(type(x))
```

---

### float (Floating Point)

The `float` data type stores real numbers with decimal points.

- Stores decimal numbers.
- Used for real-number calculations.
- Precision depends on the system.

### Example

```python
pi = 3.14

print(pi)
print(type(pi))
```

---

### complex

The `complex` data type represents numbers with a real and an imaginary part.

- Used for mathematical and scientific calculations.
- Consists of a real and an imaginary part.
- The imaginary part is written using `j`.

### Example

```python
c = 2 + 3j

print(c)
print(type(c))
```

---

## Boolean Data Type

### bool

The `bool` data type represents truth values.

- Represents `True` or `False`.
- Used in decision making and conditional statements.
- Internally stored as integers (`True` → `1`, `False` → `0`).

### Example

```python
flag = True

print(flag)
print(type(flag))
```

---

## Text Data Type

### str (String)

The `str` data type is used to store textual data such as names, messages, and sentences.

- Stores text or characters.
- Enclosed in single or double quotes.
- Immutable.

### Example

```python
name = "Marvellous Infosystems"

print(name)
print(type(name))
```

---

# Sequence Data Types

Python provides the following sequence data types:

- `list`
- `tuple`
- `range`

## list

A list is an ordered collection used to store multiple values in a single variable.

- Ordered collection.
- Mutable.
- Allows duplicate values.
- Can store mixed data types.

### Example

```python
data = [10, 20, "Python", 3.51]

print(data)
print(type(data))
```

---

## tuple

A tuple is similar to a list but is used when the data should not be changed after creation.

- Ordered collection.
- Immutable.
- Faster than list.
- Used for fixed data.

### Example

```python
point = (10, 20)

print(point)
print(type(point))
```

---

## range

The `range` data type represents a sequence of numbers and is commonly used in loops for iteration.

- Represents a sequence of numbers.
- Commonly used in loops.
- Generates values on demand.

### Example

```python
r = range(1, 5)

print(list(r))
print(type(r))
```

### Output

```text
[1, 2, 3, 4]
<class 'range'>
```

---

# Mapping Data Type

## dict (Dictionary)

A dictionary stores data in **key-value pairs**.

- Stores data as key-value pairs.
- Keys must be unique and immutable.
- Values can be of any data type.

### Example

```python
student = {
    "name": "Piyush Khairnar",
    "age": 35
}

print(student)
print(type(student))
```

---

# Set Data Type

## set

A set is an unordered collection used to store **unique elements only**.

- Unordered collection.
- Stores unique elements only.
- Mutable.
- Useful for removing duplicates.

### Example

```python
s = {10, 20, 30, 20}

print(s)
print(type(s))
```

---

# Binary Data Types

## bytes

The `bytes` data type represents an immutable sequence of bytes.

- Immutable sequence of bytes.
- Values range from `0` to `255`.
- Used in file handling and networking.

### Example

```python
b = bytes([65, 66, 67])

print(b)
print(type(b))
```

---

## bytearray

The `bytearray` data type is the mutable version of `bytes`.

- Mutable sequence of bytes.
- Individual elements can be modified.

### Example

```python
ba = bytearray([65, 66, 67])

ba[0] = 68

print(ba)
print(type(ba))
```

---

# None Data Type

## NoneType

`NoneType` represents the **absence of a value**.

- Represents absence of value.
- Used as a placeholder or default return value.
- Similar to `null` in Java.

### Example

```python
result = None

print(result)
print(type(result))
```

---

# Data Type Summary

| Type | Name | Example |
|------|------|---------|
| `int` | Integer | `x = 11` |
| `float` | Floating-point number | `pi = 3.14` |
| `bool` | Boolean | `flag = True` |
| `str` | String | `name = "Python"` |
| `list` | List | `data = [10, 20, 30]` |
| `tuple` | Tuple | `point = (10, 20)` |
| `range` | Range | `r = range(1, 5)` |
| `dict` | Dictionary | `student = {"name": "Python"}` |
| `set` | Set | `numbers = {1, 2, 3}` |
| `bytes` | Bytes | `b = bytes([65, 66, 67])` |
| `bytearray` | Bytearray | `ba = bytearray([65, 66, 67])` |
| `complex` | Complex number | `z = 5 + 6j` |
| `NoneType` | None value | `value = None` |

---

# Functions Related to Data Types

Python provides several built-in functions to understand:

- What type of object it is.
- Where it is stored.
- How much memory it occupies.
- How it behaves.

## type() Function

The `type()` function is used to **identify the data type (class)** of an object at runtime.

Since Python is dynamically typed, `type()` is used to verify the data type of a variable.

### Syntax

```python
type(object)
```

### Example

```python
x = 10
print(type(x))

y = 3.14
print(type(y))

name = "Python"
print(type(name))
```

---

## id() Function

The `id()` function returns the unique identity of an object.

It helps understand how Python manages memory and objects.

It demonstrates that:

- Variables store references to objects.
- Immutable objects may share the same memory.

### Syntax

```python
id(object)
```

### Example

```python
a = 10
b = 10

print(id(a))
print(id(b))
```

Both variables may point to the same immutable object.

### Mutable Object Example

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))
print(id(y))
```

The two list objects have different identities.

---

## len() Function

The `len()` function returns the number of elements in a sequence or collection data type.

It helps understand:

- Size of sequence types.
- Number of elements in a collection.

### Syntax

```python
len(object)
```

### Example

```python
data = [10, 20, 30, 40]
print(len(data))

name = "Python"
print(len(name))

s = (1, 2, 3)
print(len(s))
```

---

## getsizeof() Function

The `getsizeof()` function returns the **memory size in bytes** occupied by an object.

It helps understand:

- Memory usage.
- Difference between data types.
- Performance considerations.

### Syntax

```python
from sys import getsizeof

getsizeof(object)
```

### Example

```python
from sys import getsizeof

x = 10

print(getsizeof(x))
```

The memory size may vary depending on the system.

---

## isinstance() Function

The `isinstance()` function checks whether an object belongs to a specified data type.

It is useful in:

- Validations.
- Conditions.
- Real-world programs.

### Syntax

```python
isinstance(object, datatype)
```

### Example

```python
x = 10

print(isinstance(x, int))
print(isinstance(x, float))
```

### Output

```text
True
False
```

---

## hash() Function

The `hash()` function returns the hash value of an object.

It is used internally in dictionaries and sets.

- Immutable objects can be hashable.
- Mutable objects cannot be hashed in the same way.

### Example

```python
x = 10
print(hash(x))

s = "Python"
print(hash(s))
```

---

# Important Points

- A data type defines the type of a value and the operations that can be performed on it.
- In Python, everything is an object.
- Every object has a value, data type, and memory address.
- Python is dynamically typed.
- Variables are references to objects.
- The object carries the type information, not the variable itself.
- `int`, `float`, and `complex` are numeric data types.
- `bool` represents `True` or `False`.
- `str` is used for textual data.
- `list`, `tuple`, and `range` are sequence data types.
- `dict` is a mapping data type.
- `set` stores unique elements.
- `bytes` is immutable binary data.
- `bytearray` is mutable binary data.
- `NoneType` represents the absence of a value.
- `type()` identifies the type/class of an object.
- `id()` returns the identity of an object.
- `len()` returns the number of elements.
- `getsizeof()` returns the memory size in bytes.
- `isinstance()` checks whether an object belongs to a specified type.
- `hash()` returns the hash value of an object.

---

# Quick Revision

- Data Type → Defines the type of a value.
- Dynamic Typing → Type is determined at runtime.
- Variable → Reference to an object.
- `int` → Whole numbers.
- `float` → Decimal numbers.
- `complex` → Real + imaginary part.
- `bool` → `True` / `False`.
- `str` → Text.
- `list` → Ordered + Mutable.
- `tuple` → Ordered + Immutable.
- `range` → Sequence of numbers.
- `dict` → Key-value pairs.
- `set` → Unique elements.
- `bytes` → Immutable binary data.
- `bytearray` → Mutable binary data.
- `NoneType` → Absence of value.
- `type()` → Identifies object type.
- `id()` → Object identity.
- `len()` → Number of elements.
- `getsizeof()` → Memory size.
- `isinstance()` → Checks object type.
- `hash()` → Hash value.