# ============================================================
# Modules, Packages, File Handling & Exception Handling
# ============================================================

# ── MODULES & IMPORTS ────────────────────────────────────────
import os
import sys
import json
import random
import datetime
from pathlib import Path
from collections import Counter, defaultdict

# os module
print(os.getcwd())                      # current directory
print(os.path.exists("/tmp"))           # True
home = Path.home()
print(home)

# random module
print(random.randint(1, 100))           # random int 1–100
print(random.choice(["a", "b", "c"]))  # random element
nums = list(range(10))
random.shuffle(nums)
print(nums)

# datetime module
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
today = datetime.date.today()
print(today)
delta = datetime.timedelta(days=7)
print(today + delta)                    # one week from today

# collections
words = "the quick brown fox the fox".split()
counts = Counter(words)
print(counts)                           # Counter({'the': 2, 'fox': 2, ...})
print(counts.most_common(2))

dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print(dict(dd))

# ── FILE HANDLING ────────────────────────────────────────────
# Writing a file
with open("/tmp/sample.txt", "w") as f:
    f.write("Line 1: Hello Python\n")
    f.write("Line 2: File Handling\n")
    f.write("Line 3: Easy as pie\n")

# Reading entire file
with open("/tmp/sample.txt", "r") as f:
    content = f.read()
print(content)

# Reading line by line
with open("/tmp/sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# Appending
with open("/tmp/sample.txt", "a") as f:
    f.write("Line 4: Appended!\n")

# JSON read/write
data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}
with open("/tmp/data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("/tmp/data.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])               # Alice

# ── EXCEPTION HANDLING ───────────────────────────────────────
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Multiple except clauses
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        return f"Cannot convert '{value}' to int"
    except TypeError:
        return f"Wrong type: {type(value)}"

print(safe_convert("42"))       # 42
print(safe_convert("hello"))    # Cannot convert...
print(safe_convert(None))       # Wrong type...

# else and finally
def read_file(path):
    try:
        with open(path) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    else:
        print("File read successfully")
        return content
    finally:
        print("(always runs)")

read_file("/tmp/sample.txt")
read_file("/tmp/nonexistent.txt")

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)

# Custom exceptions
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount  = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100, 250)
except InsufficientFundsError as e:
    print(e)
