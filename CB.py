from CBadas import *

adasok : list[adas] = []

file = open('cb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    adasok.append(adas(row.strip))
    file.close()

print('3.feladat: CB-rádio')
print(f'3.2 feladat: Bejegyzések: {len(adasok)} db')

sanyidb = 0
for item in adasok:
    if item.nev == 'Sanyi':
        sanyidb += 1
print(f'3.3 feladat: Sanyihoz tartózó bejegyzések {sanyidb} db')

legtobb = adasok[0]
for item in adasok:
    if item.adasdb > legtobb.adasdb:
        legtobb = item

for item in adasok:
    if item.adasdb == legtobb.adasdb:
        print(f'Idő: {legtobb.ora}:{legtobb.perc} Darab: {legtobb.adasdb} Név: {legtobb.nev}')

file = open('cb2.txt', 'w', encoding='utf-8')
file.write('Kezdes;Nev;AdasDB')
for item in adasok:
    file.write(f'{item.kezdes}; {item.nev}; {item.adasdb}')
file.close()

stat = {}
for item in adasok:
    if item.nev in stat.keys():
        stat[item.nev] += item.adasdb
    else:
        stat[item.nev] = item.adasdb

print('+1 feladat: Statisztika')
for key,value in stat.items():
    print(f'\t{key}: {value}')