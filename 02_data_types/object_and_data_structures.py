# ============================================================
# Object & Data Structures 1 & 2
# ============================================================
# In Python, EVERYTHING is an object — every value has a type,
# an identity (id), and a set of methods.
#
# Built-in data types overview:
#   Text:      str
#   Numeric:   int, float, complex
#   Sequence:  list, tuple, range
#   Mapping:   dict
#   Set types: set, frozenset
#   Boolean:   bool
#   Binary:    bytes, bytearray, memoryview
#   None:      NoneType
# ============================================================

# ── EVERY VALUE IS AN OBJECT ─────────────────────────────────
x = 42
print(type(x))          # <class 'int'>
print(id(x))            # memory address
print(dir(x))           # all methods on an int

# ── NUMERIC TYPES ────────────────────────────────────────────
i = 100                 # int  — unlimited precision
f = 3.14                # float — 64-bit IEEE 754
c = 2 + 3j              # complex

print(isinstance(i, int))       # True
print(isinstance(f, float))     # True
print(c.real, c.imag)           # 2.0  3.0

# int methods
print(bin(255))         # '0b11111111'  binary
print(hex(255))         # '0xff'        hex
print(oct(255))         # '0o377'       octal
print((255).bit_length())   # 8

# float gotcha
print(0.1 + 0.2)                # 0.30000000000000004  (floating point!)
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3  (exact)

# ── SEQUENCES ────────────────────────────────────────────────
# Common operations across str, list, tuple, range:
for seq in ["hello", [1, 2, 3], (4, 5, 6)]:
    print(f"{type(seq).__name__}: len={len(seq)}, "
          f"first={seq[0]}, last={seq[-1]}, "
          f"slice={seq[1:]}")

# range — lazy sequence of integers
r = range(0, 20, 3)
print(list(r))          # [0, 3, 6, 9, 12, 15, 18]
print(10 in r)          # False
print(len(r))           # 7

# ── MUTABLE vs IMMUTABLE ─────────────────────────────────────
# Immutable: int, float, str, tuple, bool, frozenset, bytes
# Mutable:   list, dict, set, bytearray

# Immutable — cannot change in place
s = "hello"
# s[0] = "H"  ← TypeError!
s = s.replace("hello", "Hello")    # creates a new string

# Mutable — can change in place
lst = [1, 2, 3]
lst[0] = 99
lst.append(4)
print(lst)              # [99, 2, 3, 4]

# Tuples vs Lists
coords_tuple = (10.5, 20.3)   # immutable — good for fixed data
coords_list  = [10.5, 20.3]   # mutable   — good for changing data

# ── NONE TYPE ────────────────────────────────────────────────
val = None
print(val is None)      # True  — always use 'is' to check for None
print(type(val))        # <class 'NoneType'>

def find(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return None         # explicit "not found"

result = find([10, 20, 30], 99)
if result is None:
    print("Not found")

# ── BOOLEAN ──────────────────────────────────────────────────
# bool is a subclass of int — True == 1, False == 0
print(True + True)      # 2
print(True * 5)         # 5
print(sum([True, False, True, True]))   # 3

# ── BYTES ────────────────────────────────────────────────────
b = b"hello"            # bytes literal
print(b[0])             # 104  (ASCII for 'h')
print(b.decode("utf-8"))  # "hello"

text = "こんにちは"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))

# ── CHECKING TYPES ───────────────────────────────────────────
values = [42, 3.14, "hello", True, None, [1,2], {"a":1}, (1,2), {1,2}]
for v in values:
    print(f"  {str(v):<15} → {type(v).__name__}")

# ── OBJECT IDENTITY & EQUALITY ───────────────────────────────
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)           # True  — same value
print(a is b)           # False — different objects
print(a is c)           # True  — same object

# Copying
import copy
shallow = a.copy()              # shallow copy
deep    = copy.deepcopy(a)      # deep copy (for nested structures)

nested = [[1, 2], [3, 4]]
s_copy = nested.copy()
d_copy = copy.deepcopy(nested)

nested[0][0] = 99
print(s_copy)           # [[99, 2], [3, 4]]  — shallow: inner shared!
print(d_copy)           # [[1, 2], [3, 4]]   — deep: fully independent
