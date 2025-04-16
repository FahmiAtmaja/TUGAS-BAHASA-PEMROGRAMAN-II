matrix_a = [
    [5, 7, 9, 11, 13],
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [11, 13, 15, 17, 19],
    [10, 12, 14, 16, 18],
]

matrix_b = [
    [5, 8, 11, 14, 17],
    [2, 5, 8, 11, 14],
    [6, 10, 14, 18, 22],
    [10, 15, 20, 25, 30],
    [5, 7, 9, 11, 13],
]

result_matrix = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_b[0])):
        cell_sum = 0
        for k in range(len(matrix_b)):
            cell_sum += matrix_a[i][k] * matrix_b[k][j]
        row.append(cell_sum)
    result_matrix.append(row)

print("Matrix multiplication result:")
for row in result_matrix:
    print(row)