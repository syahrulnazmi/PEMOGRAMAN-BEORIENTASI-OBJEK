class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.age)

dog2 = Dog("Max", 4)
print(dog2.name) 
print(dog2.age)

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Kitty", 2)
print(cat1.name)
print(cat1.age) 

cat2 = Cat("Fluffy", 3)
print(cat2.name)
print(cat2.age)