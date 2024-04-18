first_number = int(input('Введите число: '))
second_number = int(input('Введите число: '))
print('_________________')
str_num1 = str(first_number)
str_num2 = str(second_number)

results = [0] * (len(str_num1) + len(str_num2))

str_num1 = str_num1[::-1]
str_num2 = str_num2[::-1]

for i in range(len(str_num1)):
    for j in range(len(str_num2)):
        results[i + j] += int(str_num1[i]) * int(str_num2[j])

carry = 0
for i in range(len(results)):
    results[i] += carry
    carry = results[i] // 10
    results[i] %= 10

while len(results) > 1 and results[-1] == 0:
    results.pop()

print(int(''.join(map(str, results[::-1]))))
