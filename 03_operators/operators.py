# ============================================================
# Python Operators — Comparison, Assignment, Identity, Membership
# ============================================================

a, b = 10, 20

# ── COMPARISON OPERATORS ─────────────────────────────────────
print(a == b)   # False  — equal
print(a != b)   # True   — not equal
print(a <  b)   # True   — less than
print(a >  b)   # False  — greater than
print(a <= b)   # True   — less than or equal
print(a >= b)   # False  — greater than or equal

# Chained comparisons (unique to Python)
x = 5
print(1 < x < 10)   # True
print(0 < x <= 5)   # True

# ── ASSIGNMENT OPERATORS ─────────────────────────────────────
n = 10
n += 5;  print(n)   # 15  — add and assign
n -= 3;  print(n)   # 12  — subtract and assign
n *= 2;  print(n)   # 24  — multiply and assign
n //= 5; print(n)   # 4   — floor divide and assign
n **= 3; print(n)   # 64  — exponent and assign
n %= 10; print(n)   # 4   — modulo and assign

# Walrus operator := (Python 3.8+)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(data)) > 5:
    print(f"Long list: {n} items")

# ── IDENTITY OPERATORS ───────────────────────────────────────
# 'is' checks if two variables point to the SAME object in memory
# '==' checks if values are EQUAL

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)   # True  — same value
print(list1 is list2)   # False — different objects
print(list1 is list3)   # True  — same object (alias)

# Small integers (-5 to 256) are cached in CPython
p = 100
q = 100
print(p is q)           # True  — cached singleton

# None check uses 'is', not '=='
val = None
print(val is None)      # True  (preferred idiom)
print(val is not None)  # False

# ── MEMBERSHIP OPERATORS ─────────────────────────────────────
# 'in' and 'not in'

fruits = ["apple", "banana", "cherry"]
print("apple"  in fruits)       # True
print("grape"  not in fruits)   # True

text = "Hello, Python!"
print("Python" in text)         # True
print("Java"   not in text)     # True

# Works on dicts (checks keys)
person = {"name": "Alice", "age": 30}
print("name" in person)         # True
print("email" not in person)    # True

# ── LOGICAL OPERATORS ────────────────────────────────────────
print(True and False)   # False
print(True or  False)   # True
print(not True)         # False

# Short-circuit evaluation
x = 0
print(x != 0 and 10 / x > 1)   # False (no ZeroDivisionError!)
print(x == 0 or  10 / x > 1)   # True  (short-circuits at x == 0)

# Truthy / Falsy values
falsy = [False, None, 0, 0.0, "", [], {}, set()]
for val in falsy:
    print(f"bool({val!r}) = {bool(val)}")
