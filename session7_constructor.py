# """ In Python, a constructor is a special method called __init__ that is automatically executed when a new object (instance) of a class is created. Its primary purpose is to initialize the object's attributes with specific values."""

# 1. Default Const
class Demo:
    def __init__(self):
        print("Default const")

    def demo_fun(self):
        print("demo method")

demo = Demo()
demo.demo_fun()

# 2. Parameterized Const
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        sum = self.a + self.b
        return sum
    
obj = A(10,20)
print(obj.sum())