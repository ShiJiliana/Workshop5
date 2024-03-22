n = int(input('Введите PIN из 4 цифр: '))
n1 = n // 1000
n2 = n // 100 % 10
n3 = n // 10 % 10
n4 = n % 10
if n // 10000 == 0 and n > 999:
    if n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4:
        if n < 1900 or n > 2050:
            print('OK')
        else:
            print('ERROR год')
    else:
        print('ERROR повтор')
else:
    print('ERROR много или мало')