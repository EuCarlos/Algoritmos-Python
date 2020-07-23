#  Elaborar um programa que leia 20 elementos numéricos inteiros em uma matriz A do tipo vetor. Construir uma matriz B de mesma dimensão com os mesmos elementos da matriz A acrescidos de 2. Colocar os elementos da matriz B em ordem crescente. Montar um trecho de pesquisa binária para pesquisar os elementos armazenados na matriz B.
A = []
B = []
for i in range(20):
    A.append(int(input('Informe um valor para a Matriz A[{}]: '.format(i))))
for i in range(20):
    B.append(A[i] + 3)
B = sorted(B)
print(B)
