def get_matrix(n, m, value):
    matrix = [[value for _ in range(m)] for _ in range(n)]
    return matrix

matrix = get_matrix(3, 4, 5)
for row in matrix:
    print(row)
