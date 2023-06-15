from math import sqrt

print("1. feladat: Háromszög területe és kerülete.")
print("Kérem a háromszög oldalait:")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
k = a + b + c
print(f'K = {k}')

s = k / 2
T = sqrt(s * (s - a) * (s - b) * (s - c))
print(f'T = {T}')