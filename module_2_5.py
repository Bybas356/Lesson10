def get_matrix(n=4, m=6, value=11):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
print(get_matrix())
