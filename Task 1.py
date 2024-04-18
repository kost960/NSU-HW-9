ent_problem = input('Введите N, d ,R: ')
problem = ent_problem.split()
N = int(problem[0])
d = int(problem[1])
R = int(problem[2])
print(2 * R * N + 2 * d)

ent_problem = input('Введите N, d ,R: ')
problem = ent_problem.split()
L = 0
N = int(problem[0])
d = int(problem[1])
R = int(problem[2])
for i in range(1, N + 1):
    if i == 1 or i == N:
        L += d
    L += 2 * R
print(L)
