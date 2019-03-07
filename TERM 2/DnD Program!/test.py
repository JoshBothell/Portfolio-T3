import random
for i in range(20):
    lines = open('spells.txt').read().splitlines()
    myline =random.choice(lines)
    print(myline)
