import random

def getInt(prompt, max, min = 1):
    while 1:
        try:
            ret = int(input(prompt))
            if ret <= max and ret >= min:
                return ret
            else:
                print("invalid")
        except:
            print("invalid")

class ListObject:
    def __init__(self, name):
        self.name = name
    def enact(self):
        print(self.name + ": enact error")

class Attack(ListObject):
    def __init__(self, attackName, description, accuracy, power):
        self.name = attackName
        self.description = description
        self.accuracy = accuracy
        self.power = power
    def enact(self, attacker, defender):
        print(attacker.name + self.description + " at " + defender.name)

        attackRoll = random.randint(1,self.accuracy)
        print(attackRoll)
        if attackRoll == 1:
            print ("miss")
        else:
            print("The blow  lands.")
            damage = random.randint(1,self.power)
            print("Dealing " + str(damage) + " damage.")
            defender.takeDamage(damage)

class Boxer:
    def __init__(self, name, player = False):
        self.name = name
        self.player = player
        self.hitsRemainig = 10
        self.accuracy = 5
        self.damage = 3
        punch = Attack("p","punch",self.accuracy + 1,1)
        kick = Attack("k","kick",self.accuracy + 1,1)
        self.attacks = [punch, kick]
    def chooseAttack(self, attacker, defender):
        if self.player:
            action =  getObjectFromList(self.name + " choose an attack.", self.attacks)
            ret = action.enact(attacker,defender)
            return ret
        else:
            result = random.choice(self.attacks).enact(attacker,defender)
            return result
    def takeDamage(self, damage):
        print("taking damage")
        self.hitsRemainig-= damage

def getObjectFromList(prompt, list):
    counter = 1
    for object in list:
        print(str(counter) + ") " + object.name)
        counter+=1
    choice = getInt(prompt,list.__len__(), 1)
    return list[choice-1]
def game():
    a = Boxer("Abe",True)
    b = Boxer("Bob")
    while a.hitsRemainig > 0 and b.hitsRemainig > 0:
        a.chooseAttack(a,b)
        b.chooseAttack(b,a)
game()