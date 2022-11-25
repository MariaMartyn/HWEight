# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной
# диагонали матрицы.

import random

rows = int(random.randint(3, 10))
columns = rows
numbers = [0] * rows

for i in range(len(numbers)):
    numbers[i] = list(random.randint(1, 9) for  _ in range(columns))

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end = ' ')
    print()

sumDiag = 0
sumM = 0
sumStr = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if i == j:
            sumDiag = numbers[i][j]
            sumM += sumDiag
    
print(f'Сумма главной диагонали равна {sumM}')
print()
sumStr = 0

for i in range(len(numbers)):
    sumStr = sum(numbers[i])  
    if sumStr > sumM:
        print(f'Сумма строки {i+1} превосходит сумму главной диагонали')
        print()



