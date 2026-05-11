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

| Folder | Topics Covered |
|--------|---------------|
| `01_basics/` | Variables, keywords, strings, numbers, type casting, formatting |
| `02_data_types/` | Lists, tuples, sets, dictionaries, object & data structures |
| `03_operators/` | Comparison, assignment, identity, membership operators |
| `04_control_flow/` | if/elif/else, for/while loops, break/continue |
| `05_functions/` | Functions, methods, lambda, built-ins |
| `06_oop/` | Classes, inheritance, encapsulation, polymorphism |
| `07_modules/` | import, packages, file handling, exceptions |
| `08_advanced/` | Comprehensions, decorators, generators |

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
