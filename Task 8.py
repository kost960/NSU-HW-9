x = int(input('Введите число: '))
quantity = 0

for i in range(1, round(x ** 0.5) + 1):
    for b in range(1, round(x ** 0.5) + 1):
        if i ** 2 + b ** 2 == x:
            quantity += 1
print(f'{quantity / 2:.0f}')
