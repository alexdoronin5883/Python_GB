# Напишите функцию для транспонирования матрицы

def transpose(a):
    rows_count = len(a)
    colums_count = len(a)
    if rows_count == colums_count == 0:
        print('None')
    new_matrix = []
    for j in range(colums_count):
        tmp = []
        for i in range(rows_count):
            tmp.append(a[i][j])

        new_matrix.append(tmp)
    return new_matrix


rows = int(input('Введите количество строк матрицы: ').strip())
colums = int(input('Введите количество столбцов матрицы : ').strip())
a = [[0] * colums for _ in range(rows)]
for i in range(rows):
     a[i] = [int(j) for j in input('Введите значение матрицы через пробел: ').strip().split(' ')]

    # print(transpose(a))
for row in transpose(a):
    if row != 0:
       print(*row)


# -----------------------------------Вариант2----------------------------------
from random import randint
from typing import List

def matrix(rows: int, colums: int, min_value: int, max_value: int) -> List[List[int]]:
    return [[randint(min_value, max_value)for _ in range(colums)]for _ in range(rows)]

def matrix_d(mass: List[List[int]]) -> None:
    for i in mass:
        print(' '.join(str(element)for element in i))

def trans_matrix(mass: List[List[int]]) -> List[List[int]]:
    rows = len(mass)
    colums = len(mass[0])
    trans_matrix = [[mass[j][i]for j in range(rows)]for i in range(colums)]
    return trans_matrix

rows, colums = map(int, input('Введите количество строк и столбцов матрицы через пробел: ').split())
start, stop = map(int, input('Введите минимальное и максимальное значение матрицы: ').split())
matr = matrix(rows, colums, start, stop)
t_matr = trans_matrix(matr)

matrix_d(matr)
print()
matrix_d(t_matr)