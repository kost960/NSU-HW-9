number = int(input('Введите максимальное число точек на кости: '))
quantity = 0
for i in range(1, number+1):
    quantity += i*(number+2)
print(quantity)