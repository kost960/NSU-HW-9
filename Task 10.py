def kl(k, n):
    a = 0
    if n == 0:
        return a + 1
    elif k < n:
        for i in range(k + 1, n + 1):
            a += kl(i, n - i)
        return a
    else:
        return a


n = int(input('Введите количество кубиков N: '))
print(kl(0, n))