from math import isqrt

x = int(input('Введите число: '))
results = []
for i in range(1, isqrt(x) + 1):
    yy = x - i ** 2
    y = isqrt(yy)
    if yy == 0 or y == 0:
        print('Разложение невозможно')
        break
    elif yy == y ** 2:
        res = str(i) + str(y)
        results.append(res)
        print(len(results))
        break
else:
    print('Разложение невозможно')
