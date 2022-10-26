
import random

class Hero:
    def __init__(self, name, power,armor):
        self.name = name
        self.power = power
        self.hp = 100
        self.armor = armor
        self.start_armor = armor

    def greeting(self,greeting):
        self.greeting = greeting
        return self.greeting

    def heal(self):
        if self.hp < 100:
            self.hp+=3
        if self.hp > 100:
            self.hp = 100

    def fix_armor(self):
        if self.hp == 100 and self.start_armor>= self.armor:
            self.armor+= 3
        else:
            if self.armor <= self.start_armor :
                print("Броня уже починена")

    def hit(self, enemy):
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor 
            enemy.armor = 0
        else:
            enemy.armor -= self.power
            

class Warrior(Hero):
    def __init__(self, name,power,armor):
        super().__init__(name,power,armor)
        self.hp = 100
        self.start_armor = armor
        self.tag = 'Враг'

    def ability(self):
        chance = random.randint(1,100)
        if chance > 50:
            print("Способность использована успешно. Вы увеличили свой урон")
            self.power += 2
        else:
            print("Способность использована неудачно. Вы уменьшили свой урон")
            self.power -= 1

class Magician(Hero):
    def __init__(self, name,power,armor):
        super().__init__(name,power,armor)
        self.hp = 100
        self.start_armor = armor
        self.tag = 'Маг'
        
    def ability(self): 
        chance = random.randint(1,100)
        if chance > 50:
            print("Способность использована успешно. Вы увеличили своё ХП")
            self.hp += 2
        else:
            print("Способность использована неудачно. Вы уменьшили своё ХП")
            self.hp -= 1
class tank(Hero):
    def __init__(self, name,power,armor):
        super().__init__(name,power,armor)
        self.hp = 100
        self.start_armor = armor
        self.tag = 'Танк'
        def ability(self):
            chance = random.randint(1,100)
            if chance > 50:
                print("Способность использована успешно. Вы увеличили свой урон")
                self.armor += 4
            else:
                print("Способность использована неудачно. Вы уменьшили свой урон")
                self.hp -= 2

class Asassin(Hero):
    def __init__(self, name,power,armor,plyer,enemy):
        super().__init__(name,power,armor)
        self.hp = 100
        self.start_armor = armor
        self.tag = 'Танк'
    def ability(self):
            chance = random.randint(1,100)
            if chance > 50:
                print("Способность использована успешно. Вы атаковали с удвоеным уроном.")
                self.power*=random.randint(2,3)
                player.hit(enemy)
            else:
                print("Способность использована неудачно. Вы уменьшили свой урон")
                self.hp -=  


print(tor.greeting())

print(tor.greeting())

tanos = Warrior("tanos",14, 5)
tor = Magician("tor",10, 11)
