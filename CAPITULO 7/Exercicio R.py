# Elaborar um programa que efetue a leitura de dados em duas matrizes (A e B) de uma dimensão do tipo vetor, sendo a matriz A com dez elementos e a matriz B com cinco elementos. Os elementos a serem armazenados nas matrizes devem ser do tipo cadeia. Construir uma matriz C com a capacidade de armazenar um total de 15 elementos e executar a junção das matrizes A e B na matriz C. Apresentar os dados da matriz C em ordem alfabética descendente
A = []
B = []
C = []
for i in range(10):
    A.append(str(input('Informe um valor para a Matriz A[{}]'.format(i))))
for i in range(5):
    B.append(str(input('Informe um valor para a Matriz B[{}]'.format(i))))
C = A + B
C.sort(reverse = True)
for i in range(len(C)):
    print('C[{}] = {}'.format(i, C[i]))
