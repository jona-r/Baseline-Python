# ============================================================
# Statements, Conditional Flow & Loops
# ============================================================

# ── IF / ELIF / ELSE ─────────────────────────────────────────
score = 78

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# Ternary (one-liner if/else)
status = "Pass" if score >= 60 else "Fail"
print(status)

# Nested if
age, has_id = 20, True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID")
else:
    print("Too young")

# ── FOR LOOPS ────────────────────────────────────────────────
# Iterate over a sequence
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")   # 0 2 4 6 8
print()

# enumerate — index + value
languages = ["Python", "JavaScript", "Go"]
for idx, lang in enumerate(languages, start=1):
    print(f"{idx}. {lang}")

# zip — iterate two sequences together
names  = ["Alice", "Bob", "Carol"]
scores = [95,      87,    92    ]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Nested loops — multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end="")
    print()

# ── WHILE LOOPS ──────────────────────────────────────────────
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# do-while equivalent
n = 1
while True:
    print(n, end=" ")
    n *= 2
    if n > 64:
        break
print()

# ── BREAK, CONTINUE, PASS, ELSE ──────────────────────────────
# break — exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("← stopped at 5")

# continue — skip this iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")   # odd numbers only
print()

# pass — do nothing placeholder
for i in range(3):
    pass   # loop body required, but nothing to do

# for-else / while-else — else runs if NO break occurred
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(f"{n} is prime", end=" ")   # 2 3 5 7
print()
