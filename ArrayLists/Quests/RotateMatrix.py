matrix_3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_4 = [
    [1 , 2 , 3 , 4 ],
    [5 , 6 , 7 , 8 ],
    [9 , 10, 11, 12],
    [13, 14, 15, 16]
]

def rotate_matrix(matrix):
    matrix_size = len(matrix)
    for layer in range(matrix_size // 2): # 3 = 1 Layer, 4 = 2 Layers
        for element in range(layer, matrix_size - layer - 1): # 3 and Layer 0 = [0, 1], 4 and Layer 0 = [0, 1, 2], 4 and Layer 1 = [1]
            top = matrix[layer][element]
            matrix[layer][element] = matrix[-1-element][layer]
            matrix[-1-element][layer] = matrix[-1-layer][-1-element]
            matrix[-1-layer][-1-element] = matrix[element][-1-layer]
            matrix[element][-1-layer] = top
    return matrix

def print_matrix(matrix):
    for layer in matrix:
        for element in layer:
            print(element, end = ' ')
        print("")
    print("")

def show_rotation(matrix):
    print_matrix(matrix)
    print_matrix(rotate_matrix(matrix))

show_rotation(matrix_3)
show_rotation(matrix_4)