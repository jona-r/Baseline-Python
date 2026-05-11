# Baseline Python — Course Notes & Code Examples

A complete reference repo for the **Baseline Python** course covering all 36 lessons.  
Each folder contains runnable `.py` files with examples and comments.

---

## Course Summary

Python is a high-level, interpreted, dynamically-typed language known for its clean syntax and versatility. It is used in web development, data science, automation, AI, and more.

### Key Python Features
- **Easy to read** — indentation-based syntax, no braces
- **Interpreted** — runs line by line, no compile step
- **Dynamically typed** — no need to declare variable types
- **Object-oriented** — everything is an object
- **Huge standard library** — batteries included
- **Cross-platform** — runs on Windows, macOS, Linux

---

## Folder Structure

| Folder | File | Course Lessons Covered |
|--------|------|------------------------|
| `00_intro/` | `python_intro_and_features.py` | Python Introduction, Python Features |
| `00_intro/` | `SETUP.md` | Installation: Python & pip, Installation: IDE |
| `01_basics/` | `variables_and_keywords.py` | Variable Assignment, Python Keywords |
| `01_basics/` | `strings_numbers_types.py` | Strings, Numbers, Type Casting, String Formatting |
| `02_data_types/` | `object_and_data_structures.py` | Object & Data Structures 1 & 2 |
| `02_data_types/` | `collections.py` | Lists, Tuples, Sets, Dictionaries |
| `03_operators/` | `operators.py` | Comparison, Assignment, Identity, Membership Operators |
| `04_control_flow/` | `control_flow.py` | Statements & Conditional Flow, Loops 1 & 2 |
| `05_functions/` | `functions.py` | Functions & Methods 1 & 2, Lambda, Built-in Functions |
| `06_oop/` | `oop.py` | Object Oriented Programming |
| `07_modules/` | `modules_files_exceptions.py` | Modules & Packages 1 & 2, File Handling, Exceptions 1 & 2 |
| `08_advanced/` | `advanced.py` | Comprehensions, Decorators, Generators |

---

## Quick Reference

```python
# Variables
name = "Python"
version = 3.12
is_fun = True

# String formatting
print(f"Hello from {name} {version}!")

# List, tuple, set, dict
my_list  = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set   = {1, 2, 3}
my_dict  = {"key": "value"}

# Control flow
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")

# Function
def greet(name="World"):
    return f"Hello, {name}!"

# Class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

# Lambda
square = lambda x: x ** 2

# Comprehension
evens = [x for x in range(10) if x % 2 == 0]

# Generator
def count_up(n):
    for i in range(n):
        yield i

# Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## Setup

```bash
# Check Python version (requires 3.8+)
python3 --version

# Run any example
python3 01_basics/variables.py
```

No external dependencies — pure standard library only.
