a = int(input('a = '))
b = int(input('b = '))

if a > b:
    nagyobb = a
    kisebb = b
else:
    nagyobb = b
    kisebb = a

while nagyobb != kisebb:
    nagyobb -= kisebb
    if kisebb > nagyobb:
        temp = kisebb
        kisebb = nagyobb
        nagyobb = temp

print(f'LNKO({a};{b}) = {nagyobb}')