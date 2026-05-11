# ============================================================
# Functions, Methods, Lambda & Built-in Functions
# ============================================================

# ── DEFINING FUNCTIONS ───────────────────────────────────────
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

print(greet("Alice"))

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9  (uses default exp=2)
print(power(3, 3))  # 27

# *args — variable positional arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))  # 15

# **kwargs — variable keyword arguments
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

profile(name="Alice", age=30, city="Mumbai")

# Combining all parameter types
def full_example(a, b, *args, key="default", **kwargs):
    print(f"a={a}, b={b}, args={args}, key={key}, kwargs={kwargs}")

full_example(1, 2, 3, 4, key="custom", x=10, y=20)

# ── RETURN VALUES ────────────────────────────────────────────
def min_max(lst):
    return min(lst), max(lst)   # returns a tuple

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)                   # 1 9

# ── SCOPE — LEGB rule ────────────────────────────────────────
# Local → Enclosing → Global → Built-in

x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x      # modify enclosing scope
        x = "inner"
        print(x)        # inner
    inner()
    print(x)            # inner (modified by nonlocal)

outer()
print(x)                # global (unchanged)

# ── LAMBDA FUNCTIONS ─────────────────────────────────────────
# Anonymous one-liner functions: lambda args: expression

square   = lambda x: x ** 2
add      = lambda x, y: x + y
is_even  = lambda n: n % 2 == 0

print(square(5))        # 25
print(add(3, 7))        # 10
print(is_even(4))       # True

# Lambdas with sorted / map / filter
students = [("Alice", 88), ("Bob", 75), ("Carol", 92)]
students.sort(key=lambda s: s[1], reverse=True)
print(students)         # sorted by score desc

nums = [1, 2, 3, 4, 5]
squares  = list(map(lambda x: x**2, nums))
evens    = list(filter(lambda x: x % 2 == 0, nums))
print(squares)          # [1, 4, 9, 16, 25]
print(evens)            # [2, 4]

# ── BUILT-IN FUNCTIONS ───────────────────────────────────────
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(len(data))        # 10
print(sum(data))        # 39
print(min(data))        # 1
print(max(data))        # 9
print(sorted(data))     # sorted copy
print(list(reversed(data)))

print(abs(-42))         # 42
print(round(3.14159, 2))  # 3.14

# range, enumerate, zip — already used in control_flow.py

# type and isinstance
print(type(42))                     # <class 'int'>
print(isinstance(42, (int, float))) # True
print(isinstance("hi", str))        # True

# any / all
flags = [True, False, True]
print(any(flags))       # True  — at least one True
print(all(flags))       # False — not all True

# input / print formatting
# (input() is interactive; just showing print options)
print("a", "b", "c", sep="-")      # a-b-c
print("no newline", end="")
print(" ← see?")

# id and hash
a = [1, 2, 3]
print(id(a))            # memory address

# dir — list all attributes/methods of an object
print([m for m in dir(str) if not m.startswith("_")])
