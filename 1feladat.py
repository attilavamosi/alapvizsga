for i in range(10):
    try:
        # raise ValueError('Hiba')
        a = float(input('a = '))
        b = float(input('b = '))
        print(f'T = {a * b}')
        print(f'K = {(a + b) * 2}')
    except:
    # except ValueError as error:
        print('Ez nem számbolond!')