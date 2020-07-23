# Elaborar um programa que leia 30 elementos numéricos reais em uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação: todo elemento da matriz B deve ser o cubo do elemento correspondente da matriz A. Montar o trecho de pesquisa sequencial para pesquisar os elementos armazenados na matriz B
A = []
B = []
for i in range(30):
    A.append(float(input('Informe um valor para a matriz A[i]: '.format(i))))
for i in range(30):
    B.append(A[i] ** 3)

for i in range(30):
    print(B[i])
