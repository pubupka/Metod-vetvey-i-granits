import numpy as np
from math import inf
m = inf

n = 5  # кол-во вершин и рёбер
lower_bound = 0  # нижняя граница оценки
nodes_in = [0, 1, 2, 3, 4]  # индекс вершины в списке будет индексом в матрице,
nodes_out = [0, 1, 2, 3, 4]  # это нужно для формирования списка рёбер
rebra = []

matrix = np.array([[m, 12, 22, 28, 32],
                   [12, m, 10, 40, 20],
                   [22, 10, m, 50, 10],
                   [28, 27, 17, m, 27],
                   [32, 20, 10, 60, m]])


def zero_degree(array, x, y):  # x, y - индексы нуля
    min_string = min(np.delete(array[x], y))
    min_column = min(np.delete(array[:, y], x))
    degree = min_string + min_column
    return degree


# рёбер и вершин по 5, поэтому 5 итераций, на последней остаётся только добавить оставшееся ребро
for iter in range(5):
    if iter == 4:
        rebra.append(f"({str(nodes_out[0] + 1)}, {str(nodes_in[0] + 1)})")
        break

    mins_string = []  # минимумы по строкам и столбцам
    mins_column = []
    for i in range(n):
        mins_string.append(min(matrix[i]))
        matrix[i] -= mins_string[i]
    for j in range(n):
        mins_column.append(min(matrix[:, j]))
        matrix[:, j] -= mins_column[j]  # редукция сделана
    lower_bound += sum(mins_string) + sum(mins_column)

    # подсчёт максимальной степени нуля
    degrees = {0}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                degrees.add(zero_degree(matrix, i, j))
    max_degree = max(degrees)

    # поиск нуля с максимальной степенью, его удаление и всё такое
    loop_exit = False
    for i in range(n):
        for j in range(n):
            if zero_degree(matrix, i, j) == max_degree:
                rebra.append(f"({str(nodes_out[i] + 1)}, {str(nodes_in[j] + 1)})")
                nodes_out.remove(nodes_out[i])
                nodes_in.remove(nodes_in[j])
                matrix[j][i] = inf
                matrix = np.delete(matrix, i, axis=0)
                matrix = np.delete(matrix, j, axis=1)
                n -= 1
                loop_exit = True
                break
        if loop_exit:
            break
    degrees.clear()

print("Длина маршрута:", lower_bound)
print("Маршрут образован рёбрами: ", end="")
for rebro in rebra:
    print(rebro, end=" ")
