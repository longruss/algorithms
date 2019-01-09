BOARD_SIZE = 6

def under_attack(column, queens):
    row = len(queens)+1
    for queen in queens:
        r,c = queen
        if r == row: return True # Проверяет, совпадают ли строки
        if c == column: return True # Проверяет, совпадают ли столбцы
        if (column-c) == (row-r): return True # Проверка по главной диагонали
        if (column-c) == -(row-r): return True # Проверка по побочной диагонали
    return False

def solve(n):
    if n == 0: return [[]] # Если размер поля равен нулю, возвращает пустой массив
    smaller_solutions = solve(n-1) # Нахождение подрешений через рекурсию
    return [solution+[(n, i+1)] # Возвращает решение для текущего порешения
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE): print (answer)
