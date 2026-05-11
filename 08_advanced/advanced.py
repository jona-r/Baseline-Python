# ============================================================
# Advanced Python — Comprehensions, Decorators & Generators
# ============================================================

import time
import functools

# ── COMPREHENSIONS ───────────────────────────────────────────

# List comprehension
squares  = [x**2 for x in range(1, 11)]
evens    = [x for x in range(20) if x % 2 == 0]
matrix   = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(evens)            # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(matrix)           # [[1,2,3],[2,4,6],[3,6,9]]

# Flatten a 2D list
flat = [num for row in matrix for num in row]
print(flat)

# Dict comprehension
word_lengths = {word: len(word) for word in "python is awesome".split()}
print(word_lengths)

# Set comprehension
unique_lengths = {len(word) for word in "the quick brown fox".split()}
print(unique_lengths)

# Generator expression (memory-efficient — no list created)
total = sum(x**2 for x in range(1_000_000))
print(total)


# ── DECORATORS ───────────────────────────────────────────────
# A decorator is a function that wraps another function.

# 1. Timing decorator
def timer(func):
    @functools.wraps(func)      # preserve __name__, __doc__
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"[timer] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


# 2. Logger decorator
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[log] Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__} returned {result}")
        return result
    return wrapper


# 3. Retry decorator (with arguments)
def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            raise RuntimeError(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator


# Applying decorators
@timer
@logger
def slow_sum(n):
    return sum(range(n))


@retry(times=3)
def unstable():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Flaky network")
    return "Success!"


print(slow_sum(100_000))

try:
    print(unstable())
except RuntimeError as e:
    print(e)


# Stacking decorators (applied bottom-up)
@timer
def compute(n):
    return [x**2 for x in range(n)]

compute(10_000)


# ── GENERATORS ───────────────────────────────────────────────
# Use 'yield' instead of 'return'. Lazy — values produced on demand.

# Simple generator
def count_up(start, stop, step=1):
    n = start
    while n < stop:
        yield n
        n += step

for val in count_up(0, 10, 2):
    print(val, end=" ")
print()

# Fibonacci generator (infinite!)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
first_10 = [next(gen) for _ in range(10)]
print(first_10)     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator pipeline — chaining generators
def integers(start=1):
    n = start
    while True:
        yield n
        n += 1

def take(n, iterable):
    for i, val in enumerate(iterable):
        if i >= n:
            break
        yield val

def only_evens(iterable):
    for val in iterable:
        if val % 2 == 0:
            yield val

# Compose: take first 5 even integers ≥ 1
pipeline = take(5, only_evens(integers()))
print(list(pipeline))   # [2, 4, 6, 8, 10]

# Generator vs list — memory comparison
import sys
gen_expr  = (x**2 for x in range(10_000))
list_expr = [x**2 for x in range(10_000)]
print(f"Generator size : {sys.getsizeof(gen_expr):,} bytes")
print(f"List size      : {sys.getsizeof(list_expr):,} bytes")

# send() and two-way communication
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)           # prime the generator
print(acc.send(10)) # 10
print(acc.send(20)) # 30
print(acc.send(5))  # 35
