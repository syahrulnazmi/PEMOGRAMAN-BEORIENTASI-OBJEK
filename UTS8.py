class Hero:
    def __init__(self, inputName, iputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = iputHealth
        self.power = inputPower
        self.armor = inputArmor
hero1 = Hero("pluto", 100, 10, 4)
print(float(hero1.armor))
print(float(hero1.power))
