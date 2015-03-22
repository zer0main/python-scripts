c = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
def zamena(a, b):
    for i in range(4):
        for j in range(4):
            if a == i or b == j:
                c[i][j] *= -1
def vyvod():
    for l in range(4):
        for h in  range(4):
            print(('|' if c[l][h] == 1 else '-'), end = "")
        print()
def win():
    for i in range(4):
        for j in range(4):
            if c[i][j] == 1:
                return False
    return True
h = 25
vyvod()
while not win():
    a = int(input())
    b = int(input())
    if a < 0 or b < 0 or a > 3 or b > 3:
        print('Please enter correct coordinates: ')
    else:
        zamena(a, b)
        vyvod()
    h -= 1
print('You won!')
print('Your mark', h)
