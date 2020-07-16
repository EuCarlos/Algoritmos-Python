# Elaborar um programa que leia duas matrizes A e B, cada uma de duas dimensões com cinco linhas e três colunas para valores inteiros. Construir uma matriz C de mesma dimensão, que seja formada pela soma dos elementos da matriz A com os elementos da matriz B. Apresentar os elementos da matriz C.
A = [[],[], [], [], []]
B = [[],[], [], [], []]
C = [[],[], [], [], []]
for i in range(len(A)):
    for j in range(3):
        A[i].append(int(input("Informe um valor para a Matriz A: ")))
print('='*40)
for i in range(len(B)):
    for j in range(3):
        B[i].append(int(input("Informe um valor para o Matriz B: ")))
print('='*40)
print('='*15 +' Matriz C '+ '='*15)
print('='*40)
for i in range(len(C)):
    for j in range(3):
        C[i].append(A[i][j] + B[i][j])
for i in range(len(C)):
    for j in range(3):
        print('C[{}][{}] = {}'.format(i, j, C[i][j]))
