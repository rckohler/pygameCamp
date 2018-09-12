def validateInput(prompt):
    valid = False
    while not valid:
        try:
            ret = int(input(prompt))
            valid = True
        except:
            print("invalid entry");
    return ret


class Guy:
    race = "Human"
    def __init__(self):
        self.str = 1
        self.cha = 1
        self.con = 1
        self.int = 1
        self.agi = 1
        print("You have 5 points to spend on your guy. If you spend more than that you will come into the world as a weakling")
        str = validateInput("How many points would you like to spend on strength?");
        agi = validateInput("How many points would you like to spend on agility?");
        int = validateInput("How many points would you like to spend on intelligence?");
        con = validateInput("How many points would you like to spend on consitution?");
        cha = validateInput("How many points would you like to spend on charisma?");
        if (str + agi + int + con + cha) > 5:
            print("you tried to cheat the system and are therefore cursed with weaklingness.")
        else:
            self.str += str
            self.agi += agi
            self.con += con
            self.cha += cha
            self.int += int


        self.currentHitPoints = self.con * 10
        self.maxHitPoints = self.con * 10

abe = Guy()