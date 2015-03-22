#Bot version of pilot_brothers game

import random

c = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

def change(a, b):
    for i in range(4):
        for j in range(4):
            if a == i or b == j:
                c[i][j] *= -1

def output():
    for l in range(4):
        for h in  range(4):
            print(('| ' if c[l][h] == 1 else '- '), end = "")
        print()
    print()

def win():
    for i in range(4):
        for j in range(4):
            if c[i][j] == 1:
                return False
    return True

h = 0
while not win():
    change(random.randint(0, 4), random.randint(0, 4))
    output()
    h += 1

print('Bot won!')
print('bot made', h, 'moves')
