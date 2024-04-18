for i in range(10, 99+1):
    for n in range(1, 9+1):
        if f'{i*i}' == f'{n}{i}':
            print(f'{n}{i}')