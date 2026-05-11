# ============================================================
# Strings, Numbers, Type Casting & String Formatting
# ============================================================

# ── STRINGS ─────────────────────────────────────────────────
s = "Hello, Python!"
print(len(s))                   # length
print(s.upper(), s.lower())
print(s.replace("Python", "World"))
print(s.split(", "))            # ['Hello', 'Python!']
print(s[0:5])                   # slicing → 'Hello'
print(s[-1])                    # last char → '!'
print("Python" in s)            # True

# Multiline string
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem.strip())

# Useful string methods
text = "  hello world  "
print(text.strip())             # 'hello world'
print(text.title())             # '  Hello World  '
print("hello".capitalize())    # 'Hello'
print(",".join(["a", "b", "c"]))  # 'a,b,c'
print("hello world".startswith("hello"))  # True

# ── NUMBERS ─────────────────────────────────────────────────
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

print(type(x), type(y), type(z))

# Arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (modulo)
print(10 ** 3)  # 1000 (exponent)

# math module
import math
print(math.sqrt(16))    # 4.0
print(math.floor(3.9))  # 3
print(math.ceil(3.1))   # 4
print(math.pi)          # 3.14159...
print(abs(-42))         # 42

# ── TYPE CASTING ─────────────────────────────────────────────
print(int("42"))        # str → int
print(float("3.14"))    # str → float
print(str(100))         # int → str
print(bool(0))          # 0 → False
print(bool(1))          # 1 → True
print(bool(""))         # empty string → False
print(list("abc"))      # str → ['a', 'b', 'c']

# ── STRING FORMATTING ────────────────────────────────────────
name  = "Jonathan"
score = 95.5
rank  = 1

# f-strings (Python 3.6+ — preferred)
print(f"Name: {name}, Score: {score:.1f}, Rank: #{rank}")

# .format()
print("Name: {}, Score: {:.1f}".format(name, score))

# % formatting (old style)
print("Name: %s, Score: %.1f" % (name, score))

# Alignment and padding
print(f"{'left':<10}|{'center':^10}|{'right':>10}")
print(f"{3.14159:.2f}")        # 2 decimal places
print(f"{1000000:,}")          # thousands separator → 1,000,000
print(f"{255:#x}")             # hex → 0xff
