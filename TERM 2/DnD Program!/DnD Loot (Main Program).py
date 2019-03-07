#jbothell 12/18
#dice roller prototype for D&D
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line
import random
def roll(dice):
    roll = random.randint(1, dice)
    return roll
while True:
    choice = input("""
Make A selection:
1 - Body
2 - Table
3 - 'WARNING, UNDER CONSTRUCTION'
4 - Quit
... """)
    if choice == "1":
        item_roll = roll(50)
        if item_roll > 45:
            lines = open('spells.txt').read().splitlines()
            myline =random.choice(lines)
            print("You recieve a scroll with a magical script on it, it contains the spell", myline)
        elif item_roll > 30:
            lines = open('gear.txt').read().splitlines()
            myline =random.choice(lines)
            print("You find the item: ", myline, "\nYou can find its description in the PHB")
        elif item_roll > 5:
            coins_roll = str(roll(20))
            print("You get", coins_roll, "GP")
        elif item_roll > 0:
            print("You find a health potion")
            
    elif choice == "2":
        item_roll = roll(241)
        if item_roll > 231:
            lines = open('spells.txt').read().splitlines()
            myline =random.choice(lines)
            print("You recieve a scroll with a magical script on it, it contains the spell", myline)
        elif item_roll > 221:
            lines = open('gear.txt').read().splitlines()
            myline =random.choice(lines)
            print("You find the item: ", myline, "\nYou can find its description in the PHB")
        elif item_roll > 121:
            coins_roll = str(roll(12))
            print("You get", coins_roll, "GP")
        elif item_roll > 21:
            coins_roll = str(roll(20))
            print("You get", coins_roll, "SP")
        elif item_roll > 1:
            trinket_roll = str(roll(100))
            print("You get a new trinket! Number", trinket_roll, "on the chart in the PHB")
        elif item_roll > 0:
            print("You find a locked box!")
            while True:
                opened = input("attempt to open the box as the DM directs. Do you open it? y/n ")
                if opened == "y":
                    coins_roll = str(roll(100))
                    print("You find", coins_roll, "GP inside!")
                    break
                elif opened == "n":
                    print("You fail to open the box, you leave it where you found it.")
                    break
                else:
                    print("That was not a valid y/n answer, try again")
                    
#    elif choice == "3":
    elif choice == "4":
        break
    else:
        print("That was not a valid input, Try again")
                  
