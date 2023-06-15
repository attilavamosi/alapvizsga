from random import randint

def halmaze(lista):
    halmaz = []
    for item in lista:
        if item not in halmaz:
            halmaz.append(item)
    return len(lista) == len(halmaz)

print('Halmaze?')
for i in range(8):
    lista = []
    for j in range(5):
        lista.append(randint(0,9))
        print(lista)
    print(f'{i+1}. {lista}', end='')
    if halmaze(lista):
        print('-> Halmaz.')
    else:
        print('-> Nem halmaz.')