from Toto import *

fordulok : list[Totó] = []
file = open('toto.txt','r',encoding='Utf-8')
file.readline()
for row in file:
    fordulok.append(Totó(row.strip()))
file.close()

print(f'Fordulók száma:{len(fordulok)}')

osszes = 0
for item in fordulok:
    osszes += item.t13p1
print(f'Szelvények száma: {osszes}')

for item in fordulok:
    if 'X' not in item.eredménye:
        print('Volt olyan ami nem döntetlen.')
        break
else:
    print('Mindenhol volt döntetlen.')