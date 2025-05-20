class Hero:
    jumlah = 0
    def __init__(self, inputName, iputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = iputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += -2
        print("perintah cetak Hero :" +inputName)

hero1 = Hero("pluto", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("marsa", 100, 15, 1)
print(Hero.jumlah)