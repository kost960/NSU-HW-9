quantity = int(input('Введите количество веревок для этой команды: '))
teams = 0

while quantity != 0:
    if quantity % 4 == 0:
        teams += 1
        quantity = int(input('Введите количество веревок для этой команды: '))
    else:
        quantity = int(input('Введите количество веревок для этой команды: '))
print(teams)
