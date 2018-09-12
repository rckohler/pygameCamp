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
    def __init__(self, attackName, accuracy, power):
        self.name = attackName
    def enact(self):
        print(self.name + ":default enact")
        return 1


class Boxer:
    def __init__(self, name, player = False):
        self.name = name
        self.player = player
        self.hitsRemainig = 10
        punch = Attack("punch")
        kick = Attack("kick")
        self.attacks = [punch, kick]
    def chooseAttack(self):
        if self.player:
            action =  getObjectFromList("Choose an attack",self.attacks)
            ret = action.enact()
            return ret
        else:
            result = random.choice(self.attacks).enact()
            return result
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
        b.hitsRemainig -=a.chooseAttack()
        a.hitsRemainig -=b.chooseAttack()
game()