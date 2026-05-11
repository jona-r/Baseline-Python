# ============================================================
# Variables & Python Keywords
# ============================================================

# --- Variable Assignment ---
name    = "Alice"          # str
age     = 25               # int
height  = 5.6              # float
is_dev  = True             # bool
nothing = None             # NoneType

print(type(name), type(age), type(height), type(is_dev), type(nothing))

# Multiple assignment
x = y = z = 0
a, b, c = 1, 2, 3
print(a, b, c)

# Swap without temp variable
a, b = b, a
print(a, b)

# --- Python Keywords (35 reserved words) ---
# You cannot use these as variable names:
# False, None, True, and, as, assert, async, await,
# break, class, continue, def, del, elif, else, except,
# finally, for, from, global, if, import, in, is, lambda,
# nonlocal, not, or, pass, raise, return, try, while, with, yield

import keyword
print("\nAll Python keywords:")
print(keyword.kwlist)

# --- Naming conventions ---
snake_case_var  = "preferred for variables/functions"
PascalCaseClass = "preferred for classes"
CONSTANT_VALUE  = 42        # ALL_CAPS for constants
_private        = "single underscore = private by convention"
__dunder__      = "double underscore = special/magic"
