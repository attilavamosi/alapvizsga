from random import randint
from math import sqrt

def ezprim(szam):
    for i in range(2,szam-1):
        if szam % i == 0:
            return False
    return True

szamok = []

for i in range(10):
    szamok.append(randint(10,99))

print(szamok)

for item in szamok:
    if ezprim(item) == True:
        print('Van prím')
        break
else:
    print('Nincs prím.')