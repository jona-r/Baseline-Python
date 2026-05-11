# ============================================================
# Python Introduction & Features
# ============================================================
# Python was created by Guido van Rossum, first released 1991.
# Named after Monty Python (not the snake!).
# Governed by the Python Software Foundation (PSF).
# Current stable version: Python 3.x
#
# WHY PYTHON?
#   - Simple, readable syntax (reads almost like English)
#   - Interpreted — no compilation step, run directly
#   - Dynamically typed — no need to declare variable types
#   - Garbage collected — automatic memory management
#   - Multi-paradigm: procedural, OOP, functional
#   - Huge ecosystem: 400,000+ packages on PyPI
#   - Used in: web dev, data science, AI/ML, automation, scripting
# ============================================================

# ── 1. SIMPLE & READABLE ─────────────────────────────────────
# Compare Python vs other languages for "Hello, World!":
#   Java:   System.out.println("Hello, World!");
#   C:      printf("Hello, World!\n");
#   Python: print("Hello, World!")  ← that's it

print("Hello, World!")

# ── 2. INTERPRETED ───────────────────────────────────────────
# Python executes line by line via the CPython interpreter.
# You can also run interactively in the REPL:
#   $ python3
#   >>> 2 + 2
#   4
import sys
print(f"Python version: {sys.version}")
print(f"Interpreter:    {sys.executable}")

# ── 3. DYNAMICALLY TYPED ─────────────────────────────────────
# Types are determined at runtime, not compile time.
x = 10          # int
x = "ten"       # now str — perfectly valid
x = [1, 2, 3]   # now list
print(type(x))  # <class 'list'>

# ── 4. INDENTATION BASED ─────────────────────────────────────
# Python uses whitespace (4 spaces) instead of { } braces.
# Consistent indentation IS the syntax — not optional style.
def check(n):
    if n > 0:
        print("positive")
    else:
        print("non-positive")

check(5)

# ── 5. EVERYTHING IS AN OBJECT ───────────────────────────────
# Even functions, classes and modules are first-class objects.
def say_hi():
    return "hi"

greeting = say_hi          # assign function to variable
print(greeting())          # hi
print(type(say_hi))        # <class 'function'>
print(type(int))           # <class 'type'>

# ── 6. BATTERIES INCLUDED ────────────────────────────────────
# Rich standard library — no install needed.
import os, sys, math, random, datetime, json, re, collections
print("Standard library modules loaded OK")

# ── 7. CROSS-PLATFORM ────────────────────────────────────────
print(f"Running on: {sys.platform}")   # linux / win32 / darwin

# ── 8. POPULAR USE CASES ─────────────────────────────────────
use_cases = {
    "Web Development":      ["Django", "Flask", "FastAPI"],
    "Data Science":         ["NumPy", "Pandas", "Matplotlib"],
    "Machine Learning":     ["TensorFlow", "PyTorch", "scikit-learn"],
    "Automation/Scripting": ["Selenium", "Playwright", "Paramiko"],
    "DevOps":               ["Ansible", "Fabric", "boto3"],
}
for domain, tools in use_cases.items():
    print(f"  {domain}: {', '.join(tools)}")

# ── 9. ZEN OF PYTHON ─────────────────────────────────────────
import this   # prints the 19 guiding principles of Python
