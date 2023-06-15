from epület import *

epuletek : list[Épület] = []

file = open('legmagasabb.txt','r',encoding='utf-8')
file.readline()
for row in file:
    epuletek.append(Épület(row))
file.close()

print(f'Épületek száma: {len(epuletek)} darab.')

emeletosszeg = 0
for item in epuletek:
    emeletosszeg += item.emelet
print(f'Emeletek összege: {emeletosszeg}.')


emeletosszeg = 0
for item in epuletek:
    if item.varos == 'London':
        emeletosszeg += item.emelet
print(f'Emeletek összege: {emeletosszeg}.')

legmagasabb = epuletek[0]
for item in epuletek:
    if item.magasság > legmagasabb.magasság:
        legmagasabb = item
print('A legmagasabb épület adatai:')
print(f'\tNév: {legmagasabb.név}')
print(f'\tVáros: {legmagasabb.város}')
print(f'\tOrszág: {legmagasabb.ország}')
print(f'\tMagasság: {legmagasabb.magasság}')
print(f'\tEmelet: {legmagasabb.emelet}')
print(f'\tÉpülés éve: {legmagasabb.épült}')

for item in epuletek:
    if item.ország == 'Olaszország':
        print('Van olasz épület.')
        break
else:
    print('Nincs olasz épület.')

stat = {}
for item in epuletek:
    if item.ország in stat.keys():
        stat[item.ország] += 1
    else:
        stat[item.ország] = 1

for key,value in stat.items():
    print(f'\t{key}: {value}')