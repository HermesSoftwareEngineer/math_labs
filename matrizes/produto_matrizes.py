

def somatorio(u, v, n):
    return

def produto_matrizes(matriz_A, matriz_B):
    linhas = len(matriz_A)
    colunas = len(matriz_B[0])
    print(f"Linhas e colunas: {linhas} e {colunas}")
    matriz_C = []

    for i in range(linhas):
        matriz_C.append([])
        for j in range(colunas):
            item = matriz_A[i][j]*matriz_B[j][i]
            matriz_C[i].append(item)
            print(f"Adicionado em [{i+1}][{j+1}]: {item}")

    return matriz_C


matriz_A = [
    [1, 2, 3],
    [2, 1, -1]
]

matriz_B = [
    [-1],
    [2],
    [4]
]

print(produto_matrizes(matriz_A, matriz_B))