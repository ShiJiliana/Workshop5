n = int(input('Введите число: '))
save_n = n
reversed_n = 0

while n > 0:
    number = n % 10
    reversed_n = reversed_n * 10 + number
    n = n // 10

if save_n == reversed_n:
    print('Число палиндром')
else:
    print('Не является палиндромом')

