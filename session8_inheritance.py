# """Inheritance is a core concept in Python's Object-Oriented Programming (OOP) that allows one class to derive or "inherit" attributes and methods from another class. It represents an "is-a" relationship (e.g., a Dog is an Animal)."""


# 1. Single inheritance
class Single1:
    def fun1(self):
        print("Single1 class")

class Single2(Single1):
    def __init__(self):
        print("Single2 class")
        
    def fun2(self):
        print("Single2 fun2")

single2 = Single2()
single2.fun1()
single2.fun2()

# 2. Multiple inheritance
class Multiple1:
    def __init__(self):
        print("Multiple1")

class Multiple2:
    def __init__(self):
        print("Multiple2")

class Multiple3(Multiple1, Multiple2):
    def __init__(self):
        print("Multiple3")

multi3 = Multiple3()

# 3. Multi-level inheritance
class MutliLevel1:
    def __init__(self):
        print("MutliLevel1")

class MutliLevel2(MutliLevel1):
    def __init__(self):
        print("MutliLevel2")

class MutliLevel3(MutliLevel2):
    def __init__(self):
        print("MutliLevel3")

multilevel3 = MutliLevel3()

# 4. Hierarchical Inheritance
class Shape:
    def __init__(self):
        print("Shape")

class Circle(Shape):
    def __init__(self):
        super().__init__()
        print("Circle")

class Square(Shape):
    def __init__(self):
        super().__init__()
        print("Square")

c = Circle()
s = Square()
