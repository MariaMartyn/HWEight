# Задача 1. В каждой группе учится от 20 до 30 студентов. 
# По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.

import random

rows = 10
numbers = [0] * rows

for i in range(len(numbers)):
    numbers[i] = list(random.randint(2, 5) for  _ in range(random.randint(20, 30)))

for row in numbers:
    print(row)

middle = 0
max = 0
betterGroup = 0

for i in range(len(numbers)):
    middle = round(sum(numbers[i])/len(numbers[i]), 2)
    print(f'Средний балл группы {i+1} равен {middle}')
    if middle > max: 
        max = middle
        betterGroup = i+1
    
print()
print(f'Группа с лучшим средним баллом {betterGroup}')
