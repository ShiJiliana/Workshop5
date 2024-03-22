n = int(input('Введите количество попугаев до 100: '))
if n == 1:
    print(n, 'попугай')
elif 2 <= n <= 4:
    print(n, 'попугая')
elif 5 <= n <= 20:
    print(n, 'попугаев')
elif n % 10 == 1:
    print(n, 'попугай')
elif 2 <= n % 10 <= 4:
    print(n, 'попугая')
elif 5 <= n % 10 <= 9 or n % 10 == 0:
    print(n, 'попугаев')