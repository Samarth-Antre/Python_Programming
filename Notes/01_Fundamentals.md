# Fundamentals

## Overview

Python is a **high-level, general-purpose programming language** known for its simple and readable syntax.

A Python program is a collection of instructions written to perform a specific task. This chapter introduces the basic structure of a Python program and its execution process.

---

## First Python Program

```python
print("Jay Ganesh...")
```

### Output

```text
Jay Ganesh...
```

---

## Python Source File

Python source code is stored in a file with the `.py` extension.

### Example

```text
001_First_Program.py
```

---

## Running the Program

Python programs can be executed using the Python interpreter.

### Command

```bash
python 001_First_Program.py
```

On systems where Python 3 is invoked using `python3`:

```bash
python3 001_First_Program.py
```

---

## Program Components

| Component | Description |
|-----------|-------------|
| `print()` | Built-in function used to display output. |
| `input()` | Built-in function used to accept input from the user. |
| `" "` | Represents a string literal. |
| `()` | Used for function calls and passing arguments. |
| `#` | Indicates a single-line comment. |
| Indentation | Defines the block structure of Python code. |
| `.py` | Extension used for Python source files. |

---

## User Input

The `input()` function is used to accept input from the user during program execution.

### Syntax

```python
variable = input()
```

### Example

```python
print("Enter your name : ")
Name = input()

print("Hello", Name)
```

### Input Data Type

By default, the `input()` function returns the value entered by the user as a `str` (string).

### Example

```python
No = input()

print(type(No))
```

If the user enters:

```text
11
```

the value is treated as:

```text
"11"
```

and its data type is:

```text
<class 'str'>
```

### Important Point

- `input()` → Accepts input from the user.
- `input()` → Returns a string (`str`) by default.
- Type conversion is required when numeric input is needed.

---

## Program Structure

```text
Python Source Code (.py)
          │
          ▼
Python Interpreter
          │
          ▼
Program Execution
          │
          ▼
Output
```

---

## Python vs C++

| Python | C++ |
|--------|-----|
| `print()` | `cout` |
| `input()` | `cin` |
| No mandatory `main()` function | `main()` is the entry point |
| Indentation defines blocks | `{ }` define blocks |
| `.py` | `.cpp` |
| Dynamically Typed | Statically Typed |
| Bytecode-Based Execution | Native Machine Code |
| Semicolons generally not required | Statements generally end with `;` |

---

## Important Points

- Python source files use the `.py` extension.
- Python does not require a `main()` function for a basic program.
- `print()` is used to display output.
- `input()` is used to accept user input.
- By default, `input()` returns a value of type `str`.
- Python uses indentation to define blocks of code.
- Python is dynamically typed.
- Semicolons are generally not required at the end of statements.
- The Python interpreter executes Python programs.
- Python programs can be executed using the `python` command.

---

## Quick Revision

- `.py` → Python source file
- `print()` → Displays output
- `input()` → Accepts user input
- `input()` → Returns `str` by default
- `()` → Function call
- `#` → Single-line comment
- Indentation → Defines blocks
- `main()` → Not mandatory for a basic program
- Typing → Dynamically Typed
- Interpreter → Executes Python program
- Command → `python 001_First_Program.py`