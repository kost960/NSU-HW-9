ice_cream = int(input('Введите количество упаковок мороженого: '))
people = 2
for i in range(ice_cream+1, 2, -1):
    if ice_cream % i == 0:
        people = i
print(people)