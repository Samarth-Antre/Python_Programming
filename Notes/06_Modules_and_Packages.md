# Modules and Packages

## Overview

A **module** is a Python file (`.py`) that contains reusable code, such as variables, functions, and classes.

A **package** is a way to organize related Python modules into a directory structure.

Modules and packages help keep programs organized, reusable, and easier to maintain.

---

## Why Use Modules?

Modules help programmers:

- Reuse functions in different programs.
- Divide a large program into smaller files.
- Keep related functionality together.
- Make code easier to read, test, and maintain.

---

## Types of Modules

### 1. Built-in and Standard-Library Modules

Python provides modules that can be imported without installing an additional package.

Examples:

```python
import math
import random
import os
```

A module provides functionality through the names it defines. For example, `math` provides mathematical functions and constants.

### 2. User-Defined Modules

A **user-defined module** is a Python file created by the programmer to store reusable code.

In the current examples, `Marvellous.py` is a user-defined module.

---

## Creating a User-Defined Module

Create a file named `Marvellous.py`.

### `Marvellous.py`

```python
def Addition(No1, No2):
    Ans = No1 + No2
    return Ans


def Subtraction(No1, No2):
    Ans = No1 - No2
    return Ans
```


---

## Importing a Module

The `import` statement makes a module available to the current program.

### Example: `001_Import_Module.py`

```python
import Marvellous


def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Marvellous.Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Marvellous.Subtraction(Value1, Value2)
    print("Subtraction is : ", Ret)


if __name__ == "__main__":
    main()
```

Here:

- `import Marvellous` imports the module.
- `Marvellous.Addition(...)` calls the `Addition()` function from that module.
- `Marvellous.Subtraction(...)` calls the `Subtraction()` function from that module.
- `module_name.function_name()` accesses a function through its module.

The module filename is `Marvellous.py`, but the import statement uses `Marvellous` without the `.py` extension.

---

## Example Execution

```text
Enter first number : 20
Enter second number : 10
Addition is :  30
Subtraction is :  10
```

---

## Other Import Forms

Python supports several import styles.

### Import the Module Using an Alias

```python
import Marvellous as MI

Ans = MI.Addition(10, 20)
print(Ans)
```

`MI` is an alias for the module name `Marvellous`.

### Import Specific Functions

```python
from Marvellous import Addition, Subtraction

Ans = Addition(10, 20)
print(Ans)
```

The imported function names can be used directly.

### Import All Public Names

```python
from Marvellous import *
```

This form is available, but explicit imports are usually easier to read because they make it clear which names the program uses.

---

## The `if __name__ == "__main__"` Check

A module may contain functions that should run only when the file is executed directly, rather than when it is imported.

```python
def main():
    print("Inside main")


if __name__ == "__main__":
    main()
```

- When the file is run directly, `__name__` is set to `"__main__"`.
- When the file is imported as a module, `__name__` is set to the module's name.
- The condition prevents the guarded `main()` call from running just because the module is imported.

---

## What Is a Package?

A **package** organizes related modules in a directory. It is useful when a project grows and its code needs to be grouped by purpose.

For example, a simple package layout could be:

```text
Python_Programming/
│
└── ExamplePackage/
    ├── __init__.py
    ├── arithmetic.py
    └── messages.py
```

In this example:

- `ExamplePackage/` is the package directory.
- `arithmetic.py` and `messages.py` are modules inside the package.
- `__init__.py` is commonly used to mark and initialize a package. Some modern Python packages can also work without it.


---

## Module vs Package

| Module | Package |
|---|---|
| Usually a single Python file. | A directory that organizes related modules. |
| Example: `Marvellous.py`. | Example: `ExamplePackage/`. |
| Can define reusable functions, classes, and variables. | Groups modules into a larger structure. |
| Imported using its module name. | Its modules can be imported using package-qualified names. |

---

## Common Points to Remember

- A Python module is a `.py` file.
- A user-defined module can contain reusable functions.
- Use `import module_name` to import a module.
- Use `module_name.function_name()` to call a function through the module.
- Do not include `.py` in a normal import statement.
- The importer and module must use matching function names.
- Keep related files in suitable locations so Python can find the module.
- `if __name__ == "__main__":` is useful for separating direct execution from importing.
- A package organizes related modules in a directory.

---

## Quick Revision

- **Module** → A Python file containing reusable code.
- **User-defined module** → A module created by the programmer.
- **`import Marvellous`** → Imports the `Marvellous` module.
- **`Marvellous.Addition()`** → Calls a function through the module.
- **`import Marvellous as MI`** → Imports a module with an alias.
- **`from Marvellous import Addition`** → Imports a specific function.
- **`__name__`** → Identifies how a module is being executed.
- **Package** → Organizes related modules in a directory.

---

## Current Coverage

The current repository programs cover:

- Creating a user-defined module in `Marvellous.py`.
- Defining arithmetic functions in a module.
- Importing a user-defined module.
- Calling functions through a module name.
- The `if __name__ == "__main__"` entry-point check.


