import turtle as t
import math

xc = int(input('Центр XC: '))
yc = int(input('Центр YC: '))
r = int(input('Радиус окружности: '))
x = int(input('Центр X: '))
y = int(input('Центр Y: '))

t.speed(2)
t.up()
t.setposition(xc, yc - r)
t.down()
t.circle(r)

t.up()
t.setposition(x, y)
t.down()
t.color('red')
t.dot()

distance = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)

if distance < r:
    print('Точка находится внутри окружности')
elif distance == r:
    print('Точка лежит на окружности')
else:
    print('Точка находится за пределами окружности')

t.done()