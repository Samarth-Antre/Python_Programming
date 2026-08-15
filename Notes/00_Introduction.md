# Introduction

## History of Python

| Attribute | Details |
|-----------|---------|
| Creator | Guido van Rossum |
| Development Started | 1989 |
| First Public Release | 1991 |
| Developed At | Centrum Wiskunde & Informatica (CWI), Netherlands |
| Programming Paradigm | Multi-Paradigm (Procedural, Object-Oriented, Functional) |
| Language Type | High-Level, General-Purpose, Dynamically Typed Programming Language |

---

## Overview

Python is a **high-level, general-purpose programming language** created by **Guido van Rossum** with an emphasis on simplicity, readability, and ease of programming.

Python supports **procedural programming**, **object-oriented programming (OOP)**, and **functional programming**, making it suitable for software development, automation, Data Science, Artificial Intelligence, Machine Learning, Deep Learning, and many other application areas.

Before learning advanced concepts such as **Functions**, **Classes**, **Objects**, **Inheritance**, **Exception Handling**, and **Modules**, it is essential to understand the fundamentals of Python programming, its characteristics, implementations, and program execution process.

---

## Evolution of Python

```text
Python Development Started (1989)
              │
              ▼
      Python 0.9.0 (1991)
              │
              ▼
       Python 1.0 (1994)
              │
              ▼
       Python 2.0 (2000)
              │
              ▼
       Python 3.0 (2008)
              │
              ▼
       Modern Python 3.x
```

---

## Programming Languages

A **Programming Language** is a medium used to communicate with a computer by writing instructions to solve a problem.

### Types of Programming Languages

| Level | Examples |
|--------|----------|
| High-Level | C, C++, Java, Python |
| Middle-Level | Assembly Language |
| Low-Level | Machine Language (Binary) |

---

## Program vs Process

### Program

A **Program** is a collection of instructions stored on secondary storage. It is a passive entity that does not execute until it is loaded into memory.

### Process

A **Process** is a running instance of a program. Once a program is loaded into RAM and begins execution, it becomes a process.

---

## Characteristics of Python

### Simple and Easy to Learn

Python provides a simple and readable syntax that is easy to understand and write.

Its syntax is designed to reduce unnecessary complexity and make programs easier to develop and maintain.

### High-Level Programming Language

Python is a **high-level programming language**.

It hides many low-level implementation details and allows programmers to focus mainly on application logic and problem solving.

### Interpreted Programming Language

Python is commonly described as an **interpreted programming language**.

In the standard **CPython** implementation, Python source code is compiled into **bytecode**, which is then executed by the **Python Virtual Machine (PVM)**.

### Dynamically Typed Programming Language

Python is a **dynamically typed programming language**.

The programmer does not need to explicitly declare the data type of a variable before assigning a value.

Example:

```python
value = 10
```

The type associated with `value` is determined at runtime.

### Object-Oriented Programming Language

Python supports **Object-Oriented Programming (OOP)**.

Important OOP concepts supported by Python include:

- Classes
- Objects
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

### Platform Independent

Python programs can run on different operating systems, including:

- Windows
- Linux
- macOS

The same Python source code can generally be executed across different platforms when the required Python environment is available.

### Rich Standard Library

Python provides a large collection of built-in modules through its **standard library**.

These modules provide functionality for:

- File Handling
- Mathematics
- Operating System Operations
- Networking
- Data Processing
- Random Number Generation

### Open Source and Free

Python is an **open-source programming language** that is freely available for use and distribution.

### Large Community Support

Python has a large global community of developers, educators, researchers, and organizations.

The ecosystem provides extensive documentation, libraries, frameworks, tutorials, and development tools.

### Supports Multiple Programming Paradigms

Python supports multiple programming paradigms:

- Procedural Programming
- Object-Oriented Programming
- Functional Programming

---

## Programming Paradigms Supported

Python supports multiple programming styles:

- Procedural Programming
- Object-Oriented Programming (OOP)
- Functional Programming

This makes Python flexible for developing different types of applications.

---

## Python Implementations

Python has multiple implementations designed for different execution environments and requirements.

### CPython

**CPython** is the default and most widely used implementation of Python.

It is implemented primarily in **C**.

### PyPy

**PyPy** is an alternative Python implementation that uses **Just-In-Time (JIT) compilation**.

### Jython

**Jython** is a Python implementation designed to run on the **Java Virtual Machine (JVM)**.

### IronPython

**IronPython** is a Python implementation designed to integrate with the **.NET ecosystem**.

### MicroPython

**MicroPython** is a lightweight implementation of Python designed for:

- Microcontrollers
- Embedded Systems
- Resource-constrained devices

---

## Python Source File

Python source code is stored in a file with the `.py` extension.

Example:

```text
Demo.py
```

The `.py` file contains the Python source code written by the programmer.

---

## Python Virtual Machine (PVM)

**PVM** stands for **Python Virtual Machine**.

The PVM is the runtime engine responsible for executing Python bytecode.

### Responsibilities of PVM

- Executes Python bytecode.
- Manages runtime memory.
- Manages object references.
- Handles exceptions.
- Supports garbage collection.
- Controls runtime execution.

---

## Build Process of Python

Python source code passes through several stages before and during execution.

### Build Process Flow

```text
Python Source Code (.py)
          │
          ▼
Lexical Analysis / Tokenization
          │
          ▼
Parsing
          │
          ▼
Abstract Syntax Tree (AST)
          │
          ▼
Compilation to Bytecode
          │
          ▼
Python Bytecode
          │
          ▼
Python Virtual Machine (PVM)
          │
          ▼
Program Execution
```

---

## Lexical Analysis

During **Lexical Analysis**, Python source code is processed into smaller meaningful units called **tokens**.

Examples of tokens include:

- Keywords
- Identifiers
- Literals
- Operators
- Delimiters

---

## Parser

The **Parser** validates the syntax and structure of the Python program.

It processes the tokens and forms the logical structure of the program.

The resulting structure can be represented using an **Abstract Syntax Tree (AST)**.

---

## Abstract Syntax Tree (AST)

**AST** stands for **Abstract Syntax Tree**.

An AST represents the logical structure of a Python program in a tree-like form.

It provides a structured representation of the source code before compilation into bytecode.

---

## Bytecode

In the standard **CPython** implementation, Python source code is compiled into **bytecode**.

Bytecode is an intermediate representation of the Python program that can be executed by the **Python Virtual Machine (PVM)**.

Python bytecode is commonly associated with `.pyc` files.

Example:

```text
Demo.cpython-XXX.pyc
```

---

## `__pycache__`

Python can store compiled bytecode inside a directory named:

```text
__pycache__
```

Example:

```text
Project/
│
├── Demo.py
│
└── __pycache__/
    └── Demo.cpython-XXX.pyc
```

The exact bytecode filename depends on the Python version and implementation.

---

## Complete Python Toolchain

The complete Python execution toolchain can be represented as:

```text
Editor / IDE
      │
      ▼
Python Source Code (.py)
      │
      ▼
Tokenizer / Lexer
      │
      ▼
Parser
      │
      ▼
Abstract Syntax Tree (AST)
      │
      ▼
Bytecode Compiler
      │
      ▼
Python Bytecode
      │
      ▼
Python Virtual Machine (PVM)
      │
      ▼
Standard Libraries
      │
      ▼
Third-Party Libraries
      │
      ▼
Program Execution
```

### Toolchain Components

- **Editor / IDE** – Used to write and edit Python source code.
- **Tokenizer / Lexer** – Converts source code into tokens.
- **Parser** – Validates syntax and forms the program structure.
- **AST** – Represents the logical structure of the program.
- **Bytecode Compiler** – Converts the program representation into bytecode.
- **Bytecode** – Intermediate representation executed by the PVM.
- **PVM** – Executes Python bytecode.
- **Standard Libraries** – Provide commonly required functionality.
- **Third-Party Libraries** – Provide additional functionality for specialized applications.

---

## Operating System

An **Operating System (OS)** is system software that acts as an interface between the user, application software, and computer hardware.

### Responsibilities

- File Management
- Memory Management
- Process Management
- CPU Scheduling
- Hardware Abstraction

### Examples

- Windows
- Linux
- macOS

---

## Standard Library

Python provides a large **Standard Library** containing modules for commonly required programming tasks.

Examples:

```python
import os
import math
import random
```

The standard library provides functionality without requiring separate installation.

---

## Third-Party Libraries

Python has a large ecosystem of third-party libraries.

Third-party libraries can be installed using **PIP**.

Example:

```bash
pip install package_name
```

Third-party libraries are widely used in:

- Data Science
- Machine Learning
- Artificial Intelligence
- Automation
- Web Development

---

## Why Learn Python?

Learning Python helps programmers:

- Build a strong programming foundation.
- Develop programming logic and problem-solving skills.
- Understand Object-Oriented Programming concepts.
- Develop automation scripts.
- Work with Data Science.
- Develop Machine Learning applications.
- Explore Artificial Intelligence.
- Work with Deep Learning.
- Develop Generative AI applications.
- Prepare for Software Engineering interviews.

---

## Applications of Python

Python is widely used in:

- Software Development
- Web Development
- Automation
- Scripting
- Data Science
- Machine Learning
- Artificial Intelligence
- Deep Learning
- Generative AI
- Scientific Computing
- Data Analysis
- Testing
- Embedded and IoT Applications

---

## Features of Python

- High-Level Programming Language
- General-Purpose Programming Language
- Simple and Readable Syntax
- Dynamically Typed
- Object-Oriented Programming
- Multi-Paradigm Programming
- Platform Independent
- Open Source
- Rich Standard Library
- Large Community Support
- Automatic Memory Management
- Extensive Third-Party Library Ecosystem

---

## Python vs C++

| Python | C++ |
|--------|-----|
| Dynamically Typed | Statically Typed |
| Bytecode-Based Execution | Compiled to Native Machine Code |
| Automatic Memory Management | Manual Memory Management with RAII and Other Mechanisms |
| Indentation Defines Blocks | Curly Braces `{}` Define Blocks |
| `print()` | `cout` |
| `input()` | `cin` |
| `.py` | `.cpp` |
| Python Virtual Machine (PVM) | Native Machine Code Execution |
| Supports OOP | Supports OOP |
| Supports Functional Programming | Supports Generic and Functional Programming |
| Rich Standard Library | Standard Library and STL |

---

## Python Program Execution Flow

```text
Write Python Source Code (.py)
            │
            ▼
      Lexical Analysis
            │
            ▼
          Parsing
            │
            ▼
            AST
            │
            ▼
    Compile to Bytecode
            │
            ▼
      Python Bytecode
            │
            ▼
 Python Virtual Machine (PVM)
            │
            ▼
     Program Execution
```

---

## Local Environment Setup

### Code Editor / IDE

- Visual Studio Code

### Python Interpreter

- Python

### Package Manager

- PIP

### Version Control

- Git

### Repository Hosting

- GitHub

---

## Important Points

- Python was created by **Guido van Rossum**.
- Python development started around **1989**.
- The first public release of Python was made in **1991**.
- Python is a **high-level, general-purpose programming language**.
- Python is **dynamically typed**.
- Python supports **Object-Oriented Programming**.
- Python supports **Procedural, Object-Oriented, and Functional Programming**.
- Python source files use the `.py` extension.
- In CPython, Python source code is compiled into **bytecode**.
- Python bytecode is executed by the **Python Virtual Machine (PVM)**.
- Python bytecode can be stored inside the `__pycache__` directory.
- **CPython** is the default and most widely used Python implementation.
- Python is widely used in **Data Science, Machine Learning, Artificial Intelligence, Automation, and Software Development**.

---

## Quick Revision

- Creator → **Guido van Rossum**
- Development Started → **1989**
- First Public Release → **1991**
- Source File → **`.py`**
- Bytecode → **`.pyc`**
- Runtime Engine → **Python Virtual Machine (PVM)**
- Default Implementation → **CPython**
- Syntax Representation → **AST**
- Bytecode Cache → **`__pycache__`**
- Typing → **Dynamically Typed**
- Programming Style → **Procedural + Object-Oriented + Functional**
- Package Manager → **PIP**
- Code Editor → **Visual Studio Code**
- Version Control → **Git**
- Repository Hosting → **GitHub**