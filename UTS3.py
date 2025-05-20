class Dog:
    kind = "Toys"
    def __init__(self, name):
        self.name = name

d = Dog("Aji")
e = Dog("Nomomo")
print(d.kind, e.name, d.name, e.name)