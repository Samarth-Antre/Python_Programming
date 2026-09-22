# Operators

## Overview

An **operator** is a symbol used to perform an operation on values or variables.

The values on which an operator operates are called **operands**.

### Example

```python
No1 = 10
No2 = 20

Ans = No1 + No2

print(Ans)
```

Here:

- `No1` and `No2` are operands.
- `+` is the operator.
- `Ans` stores the result.

---

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |

---

## Addition Operator

The `+` operator is used to perform addition.

### Syntax

```python
Operand1 + Operand2
```

### Example

```python
No1 = 10
No2 = 20

Ans = No1 + No2

print("Addition is : ", Ans)
```

### Output

```text
Addition is : 30
```

---

## Subtraction Operator

The `-` operator is used to perform subtraction.

### Syntax

```python
Operand1 - Operand2
```

### Example

```python
No1 = 20
No2 = 10

Ans = No1 - No2

print("Subtraction is : ", Ans)
```

### Output

```text
Subtraction is : 10
```

---

## Multiplication Operator

The `*` operator is used to perform multiplication.

### Syntax

```python
Operand1 * Operand2
```

### Example

```python
No1 = 10
No2 = 20

Ans = No1 * No2

print("Multiplication is : ", Ans)
```

### Output

```text
Multiplication is : 200
```

---

## Division Operator

The `/` operator is used to perform division.

### Syntax

```python
Operand1 / Operand2
```

### Example

```python
No1 = 20
No2 = 10

Ans = No1 / No2

print("Division is : ", Ans)
```

### Output

```text
Division is : 2.0
```

The `/` operator produces a floating-point result.

---

## Arithmetic Operations with User Input

The `input()` function accepts input from the user as a string.

For arithmetic operations, the input can be converted into an integer using `int()`.

### Example

```python
print("Enter first number : ")
No1 = int(input())

print("Enter second number : ")
No2 = int(input())

Add = No1 + No2
Sub = No1 - No2
Mul = No1 * No2
Div = No1 / No2

print("Addition       : ", Add)
print("Subtraction    : ", Sub)
print("Multiplication : ", Mul)
print("Division       : ", Div)
```

---

## Operators and Operands

An expression contains operators and operands.

### Example

```python
No1 + No2
```

| Element | Meaning |
|---------|---------|
| `No1` | Operand |
| `+` | Operator |
| `No2` | Operand |

The operator performs the required operation on the operands.

---

## Important Points

- Operators are used to perform operations on values and variables.
- Values on which operators operate are called operands.
- `+` performs addition.
- `-` performs subtraction.
- `*` performs multiplication.
- `/` performs division.
- `input()` returns user input as a string by default.
- `int(input())` converts user input into an integer.
- The `/` operator produces a floating-point result.
- Operators and operands together form expressions.

---

## Quick Revision

```text
Operators
    │
    └── Arithmetic Operators
            │
            ├── +  → Addition
            ├── -  → Subtraction
            ├── *  → Multiplication
            └── /  → Division
```

---

## Current Coverage

The current programs cover the basic arithmetic operators:

- Addition
- Subtraction
- Multiplication
- Division
- Arithmetic operations using user input

