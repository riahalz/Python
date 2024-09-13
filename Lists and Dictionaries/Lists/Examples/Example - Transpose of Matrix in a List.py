### Lists - Transpose of Matrix in a List ###

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed) # Output: [[1, 4], [2, 5], [3, 6], [4, 8]]
