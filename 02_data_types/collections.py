# ============================================================
# Lists, Tuples, Sets & Dictionaries
# ============================================================

# ── LISTS — ordered, mutable, allows duplicates ──────────────
fruits = ["apple", "banana", "cherry", "apple"]

print(fruits[0])            # apple  (indexing)
print(fruits[-1])           # apple  (negative index)
print(fruits[1:3])          # ['banana', 'cherry']  (slicing)

fruits.append("mango")      # add to end
fruits.insert(1, "blueberry")  # insert at index
fruits.remove("apple")      # remove first occurrence
popped = fruits.pop()       # remove & return last item
print(fruits)

# List methods
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(nums)                 # [1, 1, 2, 3, 4, 5, 6, 9]
nums.reverse()
print(nums)
print(sorted([3, 1, 2]))    # non-destructive sort

# List operations
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)                # [1, 2, 3, 4, 5, 6]
print(a * 2)                # [1, 2, 3, 1, 2, 3]
print(3 in a)               # True
print(len(a))               # 3

# ── TUPLES — ordered, immutable ──────────────────────────────
coords = (10.5, 20.3)
rgb    = (255, 128, 0)
single = (42,)              # note the trailing comma!

x, y = coords               # unpacking
print(x, y)

print(coords.count(10.5))   # 1
print(rgb.index(128))       # 1

# Tuples are faster than lists and hashable (usable as dict keys)
point_dict = {(0, 0): "origin", (1, 0): "x-axis"}

# ── SETS — unordered, unique elements ────────────────────────
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)              # union:        {1,2,3,4,5,6,7}
print(s1 & s2)              # intersection: {3,4,5}
print(s1 - s2)              # difference:   {1,2}
print(s1 ^ s2)              # symmetric diff: {1,2,6,7}

s1.add(10)
s1.discard(1)               # remove if present (no error if missing)
print(len(s1))

# Remove duplicates from a list
dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(dupes))
print(sorted(unique))       # [1, 2, 3, 4]

# ── DICTIONARIES — key-value pairs, ordered (3.7+) ───────────
person = {
    "name": "Alice",
    "age": 30,
    "city": "Mumbai",
    "skills": ["Python", "SQL"]
}

print(person["name"])               # direct access
print(person.get("salary", 0))      # safe access with default

person["email"] = "alice@example.com"  # add key
person["age"] = 31                      # update value
del person["city"]                      # delete key

print(person.keys())
print(person.values())
print(person.items())

# Iterating
for key, value in person.items():
    print(f"  {key}: {value}")

# dict methods
d = {"a": 1, "b": 2}
d.update({"b": 99, "c": 3})    # merge/update
print(d)
print(d.pop("a"))               # remove and return value

# dict comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)                  # {1:1, 2:4, 3:9, 4:16, 5:25}

# Nested dict
employees = {
    "E001": {"name": "Bob",   "dept": "Engineering"},
    "E002": {"name": "Carol", "dept": "Marketing"},
}
print(employees["E001"]["dept"])    # Engineering
