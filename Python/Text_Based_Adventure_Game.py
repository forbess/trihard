import random

class character:
    def __init__(self):
        print("Welcome to 'Text-Based Python Adventure Game!")
        self.fill_line()
        self.name = input("Type your character's name: ")
        self.health = 100
        self.lives = 3
        self.money = 15000

    def fill_line(self):
        print("-" * 50)

class weapon:
    def __init__(self):
        self.damage = 0
        self.range = 0
        self.cost = 0

        
character = character()
#SWORD
sword = weapon()
sword.cost = 10000
sword.damage = 4500
sword.range = 10
#DAGGER
dagger = weapon()
dagger.cost = 7500
dagger.damage = 3000
dagger.range = 10
#SCTYHE
scythe = weapon()
scythe.cost = 12000
scythe.damage = 6000
scythe.range = 10
#BOW
bow = weapon()
bow.cost = 8000
bow.damage = 2500
bow.range = 50
#GUN
gun = weapon()
gun.cost = 13500
gun.damage = 80000
gun.range = 75
print("Checking weapons... Done!")
character.fill_line()
# end (Kappa)




