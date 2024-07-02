# Объявите функцию get_matrix и напишите в ней параметры n, m и value.

def get_matrix(n, m, value):
    matrix = []  # Создайте пустой список matrix внутри функции get_matrix.
    if n <= 0 or m <= 0 or value <= 0:  # Отбросить любое нулевое значение n, m, value
        return matrix  # Возвращение значения matrix при любом нулевом значении n, m, value
    for i in range(n):  # Напишите первый (внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([])  # В первом цикле добавляйте пустой список в список matrix.
        for j in range(m):  # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix[i].append(value)  # Во втором цикле пополняйте ранее добавленный пустой список значениями value.
    return matrix  # После всех циклов верните значение переменной matrix.


result1 = get_matrix(2, 2, 10)  # Параметры
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Результат выводим в консоль функции get_matrix
print(result1)
print(result2)
print(result3)
