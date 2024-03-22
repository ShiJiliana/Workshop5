n = int(input('Введите кол-во кнатов: '))
galleons = n // (17*29)
knats = n - (galleons * 17 * 29)
sikls = knats // 29
knats = knats - (sikls * 29)

if galleons != 0:
    print(galleons, 'галлеонов')
if sikls != 0:
    print(sikls, 'сиклей')
if knats != 0:
    print(knats, 'кнатов')