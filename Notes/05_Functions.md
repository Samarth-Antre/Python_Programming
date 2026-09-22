# Functions

## Overview

A **function** is a block of statements designed to perform a particular task.

Functions help divide a program into smaller and manageable parts.

A function can be defined once and called whenever its functionality is required.

The current programs introduce:

- Function definition
- Function call
- Multiple function calls
- `main()` function
- `__name__`
- `if __name__ == "__main__"`

---

# Function Definition

A function is defined using the `def` keyword.

### Syntax

```python
def FunctionName():
    statements
```

### Example

```python
def Display():
    print("Inside Display")
```

Here:

- `def` is the keyword used to define a function.
- `Display` is the function name.
- `()` represents the function parameter list.
- The indented statements form the function body.

Defining a function does not execute the function body.

---

# Function Call

A function is executed when it is called.

### Example

```python
def Display():
    print("Inside Display")

Display()
```

### Output

```text
Inside Display
```

The statement:

```python
Display()
```

is the function call.

---

# Calling a Function Multiple Times

A function can be called multiple times.

### Example

```python
def Display():
    print("Inside Display")

Display()
Display()

print("End of application")
```

### Output

```text
Inside Display
Inside Display
End of application
```

Each function call executes the statements inside the function.

---

# Function Definition and Function Call

The basic execution flow is:

```text
Function Definition
        ↓
Function Call
        ↓
Function Body Execution
```

### Example

```python
def Display():
    print("Inside Display")

Display()
```

The function is first defined and then called.

---

# `main()` Function

A function named `main()` can be used to organize the main logic of a program.

### Example

```python
def main():
    print("Inside main")

main()
```

Here:

1. `main()` is defined.
2. `main()` is called.
3. The statements inside `main()` are executed.

---

# `__name__`

Python provides a special variable called:

```python
__name__
```

When a Python file is executed directly, the value of `__name__` is:

```text
__main__
```

### Example

```python
print(__name__)
```

When the file is executed directly, the output is:

```text
__main__
```

The `__name__` concept helps identify how the Python file is being executed.

---

# `if __name__ == "__main__"`

The following structure is used to check whether the current Python file is being executed directly:

```python
def main():
    print("Inside main")

if __name__ == "__main__":
    main()
```

The condition:

```python
__name__ == "__main__"
```

checks whether the current file is the main program being executed.

If the condition is true, `main()` is called.

---

# Main Function and Entry Point

A common structure for a Python program is:

```python
def main():
    print("Inside main")

if __name__ == "__main__":
    main()
```

### Execution Flow

```text
Program Starts
      ↓
main() is defined
      ↓
__name__ is checked
      ↓
__name__ == "__main__"
      ↓
main() is called
      ↓
Function body executes
```

This provides a clear entry point for the program.

---

# Function Definition vs Function Call

| Function Definition | Function Call |
|---------------------|---------------|
| Creates a function | Executes the function |
| Uses `def` | Uses the function name |
| Contains the function body | Transfers execution to the function body |

### Example

Function definition:

```python
def Display():
    print("Inside Display")
```

Function call:

```python
Display()
```

---

# Important Points

- Functions are defined using the `def` keyword.
- A function contains a block of statements.
- Defining a function does not execute its body.
- A function is executed when it is called.
- A function can be called multiple times.
- `main()` can be used to organize the main logic of a program.
- `__name__` is a special variable.
- When a file is executed directly, `__name__` has the value `"__main__"`.
- `if __name__ == "__main__":` is used as an entry-point check.
- Indentation defines the function body.

---

# Quick Revision

```text
Functions
    │
    ├── Function Definition
    │       └── def
    │
    ├── Function Call
    │       └── FunctionName()
    │
    ├── Multiple Function Calls
    │
    └── main()
            │
            └── if __name__ == "__main__"
```

---

## Current Coverage

The current  programs cover:

- Function definition
- Function call
- Multiple function calls
- `main()` function
- `__name__`
- `if __name__ == "__main__"`
- Main program entry point

