# ============================================================
# Object-Oriented Programming (OOP)
# ============================================================

# ── CLASSES & OBJECTS ────────────────────────────────────────
class Dog:
    species = "Canis familiaris"    # class attribute (shared)

    def __init__(self, name, age):  # constructor
        self.name = name            # instance attribute
        self.age  = age

    def __str__(self):              # string representation
        return f"Dog({self.name}, {self.age})"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"

    def bark(self):
        return f"{self.name} says: Woof!"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"


rex   = Dog("Rex", 3)
buddy = Dog("Buddy", 5)

print(rex)              # Dog(Rex, 3)
print(rex.bark())       # Rex says: Woof!
print(Dog.species)      # Canis familiaris
print(rex.birthday())   # Rex is now 4


# ── INHERITANCE ──────────────────────────────────────────────
class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return self.name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")   # call parent __init__

    def purr(self):
        return f"{self.name} purrs..."


class GuideDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner

    def guide(self):
        return f"{self.name} is guiding {self.owner}"


whiskers = Cat("Whiskers")
print(whiskers.speak())     # Whiskers says Meow!
print(whiskers.purr())

scout = GuideDog("Scout", 4, "John")
print(scout.bark())
print(scout.guide())
print(isinstance(scout, Dog))   # True — is-a relationship


# ── ENCAPSULATION ────────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner    = owner
        self.__balance = balance    # name-mangled → _BankAccount__balance

    @property
    def balance(self):              # getter
        return self.__balance

    @balance.setter
    def balance(self, amount):      # setter with validation
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.__balance:,.2f}"


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)              # Alice: $1,300.00
print(acc.balance)      # 1300


# ── POLYMORPHISM ─────────────────────────────────────────────
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return round(math.pi * self.radius ** 2, 2)
    def __str__(self):
        return f"Circle(r={self.radius})"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def __str__(self):
        return f"Rectangle({self.w}x{self.h})"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height
    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(f"{shape}: area = {shape.area()}")


# ── DUNDER / MAGIC METHODS ───────────────────────────────────
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)          # Vector(4, 6)
print(v1 * 3)           # Vector(3, 6)
print(len(v1))          # 2
print(v1 == Vector(1, 2))  # True
