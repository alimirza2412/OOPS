# 🐍 OOPs in Python - Complete Guide

A beginner-friendly guide to Object-Oriented Programming in Python based on handwritten notes.

## 📑 Table of Contents

- [What is OOP?](#what-is-oop)
- [Class](#class)
- [Object](#object)
- [Attributes](#attributes)
- [Methods](#methods)
- [Self](#self)
- [Constructor](#constructor)
- [Encapsulation](#encapsulation)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Method Overriding](#method-overriding)
- [Super](#super)
- [Class Variable vs Instance Variable](#class-variable-vs-instance-variable)
- [Magic Methods](#magic-methods)
- [Operator Overloading](#operator-overloading)
- [Aggregation](#aggregation)
- [Mutable vs Immutable](#mutable-vs-immutable)
- [📝 Cheat Sheet](#-cheat-sheet)
- [🚀 Quick Start](#-quick-start)

---

## What is OOP?

**OOP = Object-Oriented Programming**

It is a way of writing code by creating **objects** that represent real-life things.

**Examples:** `Car`, `Student`, `ATM`, `Mobile`

Instead of writing everything in one place, we create a **class** and then make **objects** from it.

---

## Class

A **class** is a blueprint or template.

> 💡 **Think of a house map:** The map is the class. Many houses can be built using the same map.

```python
class Student:
    pass
```

---

## Object

An **object** is the real thing made from a class.

```python
s1 = Student()  # s1 is one student
s2 = Student()  # s2 is another student
# Both are objects
```

---

## Attributes

Attributes are the **data** of objects.

A student has: `Name`, `Age`, `Roll Number`

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
print(s1.name)  # Ali
print(s1.age)   # 20
```

---

## Methods

Methods are **functions** inside a class.

A student can: `study`, `sleep`, `play`

```python
class Student:
    def study(self):
        print("Studying...")

    def sleep(self):
        print("Sleeping...")

s1 = Student()
s1.study()  # Studying...
s1.sleep()  # Sleeping...
```

---

## Self

`self` means **this current object**.

Without `self`, Python does not know which object you are talking about.

```python
class Student:
    def show_name(self, name):
        print(f"My name is {name}")

s1 = Student()
s1.show_name("Ali")  # My name is Ali
```

---

## Constructor

The **constructor** (`__init__`) runs **automatically** when an object is created.

```python
class Student:
    def __init__(self):
        print("Student created!")

s = Student()
# Output: Student created!
```

---

## Encapsulation

**Encapsulation** = Hide important data from direct access.

> Example: ATM PIN should not be changed directly.

```python
class ATM:
    def __init__(self, pin):
        self.__pin = pin  # Private variable

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin

atm = ATM(1234)
print(atm.get_pin())  # 1234
atm.set_pin(5678)
print(atm.get_pin())  # 5678
```

✅ This keeps data **safe**.

---

## Inheritance

**Inheritance** = Child class gets features of parent class.

```python
class Animal:
    def eat(self):
        print("Eating...")

    def walk(self):
        print("Walking...")

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def bark(self):
        print("Bark!")

d = Dog()
d.eat()   # Eating... (from Animal)
d.walk()  # Walking... (from Animal)
d.sleep() # Sleeping... (from Animal)
d.bark()  # Bark! (from Dog)
```

### Types of Inheritance

| Type | Description | Example |
|------|-------------|---------|
| Single | One parent → One child | A → B |
| Multiple | Two parents → One child | A → C, B → C |
| Multilevel | Grandparent → Parent → Child | A → B → C |
| Hybrid | Combination of above | Mixed |

---

## Polymorphism

**Polymorphism** = One function → Different behavior.

```python
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

d = Dog()
c = Cat()
print(d.sound())  # Bark
print(c.sound())  # Meow
# Same method name → Different output
```

---

## Method Overriding

**Method Overriding** = Child class changes the parent's method.

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()  # Bark
# Dog replaces the parent's method
```

---

## Super

`super()` is used to call the parent class.

This avoids writing the same code again.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

d = Dog("Tommy", "Labrador")
print(d.name)   # Tommy
print(d.breed)  # Labrador
```

---

## Class Variable vs Instance Variable

### Class Variable

Shared by every object.

```python
class Student:
    school_name = "ABC School"  # Class variable

s1 = Student()
s2 = Student()
print(s1.school_name)  # ABC School
print(s2.school_name)  # ABC School
```

### Instance Variable

Different for every object.

```python
class Student:
    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Ali")
s2 = Student("Ahmed")
print(s1.name)  # Ali
print(s2.name)  # Ahmed
```

---

## Magic Methods

Magic methods are special methods that Python calls automatically.

| Method | Purpose |
|--------|---------|
| `__init__` | Constructor |
| `__str__` | Print object nicely |
| `__add__` | Use `+` with your own object |

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __add__(self, other):
        return self.age + other.age

s1 = Student("Ali", 20)
s2 = Student("Ahmed", 22)
print(s1)       # Ali, 20 years old
print(s1 + s2)  # 42
```

---

## Operator Overloading

Make operators work with your own class.

> Example: Instead of `a + b`, you can write `Fraction1 + Fraction2` using `__add__()`.

```python
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.num}/{self.den}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)  # 5/6
```

---

## Aggregation

**Aggregation** = One object contains another object.

```python
class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

addr = Address("New York", "USA")
c = Customer("Ali", addr)

print(c.name)             # Ali
print(c.address.city)     # New York
print(c.address.country)  # USA
```

---

## Mutable vs Immutable

| Type | Can Change? | Examples |
|------|:-----------:|----------|
| **Mutable** | ✅ Yes | `list`, `dict`, `set` |
| **Immutable** | ❌ No | `tuple`, `str`, `int` |

### Mutable Example

```python
numbers = [1, 2]
numbers.append(3)
print(numbers)  # [1, 2, 3]
```

### Immutable Example

```python
name = "Ali"
# name[0] = "B"  # ❌ Error!
name = "Bob"     # ✅ Reassigning is allowed
```

---

## 📝 Cheat Sheet

| Concept | Meaning |
|---------|---------|
| **Class** | Blueprint (design) |
| **Object** | Real thing made from the blueprint |
| **Attribute** | Data → Name, Age, Color |
| **Method** | Action → study, drive, withdraw |
| **Constructor** | Runs automatically when object is created |
| **Encapsulation** | Hide important data |
| **Inheritance** | Child class gets parent's feature |
| **Polymorphism** | Same method, different behavior |
| **Overriding** | Child changes parent's method |
| **super()** | Call the parent class |
| **Magic Method** | Special methods: `__init__`, `__str__`, `__add__` |

---

## 🚀 Quick Start

```python
# Define a class
class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age

    def study(self):
        print(f"{self.name} is studying...")

# Create objects
s1 = Student("Ali", 20)
s2 = Student("Ahmed", 22)

# Use methods
s1.study()  # Ali is studying...
s2.study()  # Ahmed is studying...

# Access variables
print(s1.name)         # Ali
print(Student.school)  # ABC School
```

---
