import random

n = int(input())
a = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
passwd = ''
for i in range(n):
    passwd += a[random.randint(0, 61)]

print('your password:', passwd)
