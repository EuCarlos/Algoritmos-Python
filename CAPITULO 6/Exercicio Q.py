#  Elaborar um programa que leia 12 elementos inteiros para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, observando a seguinte lei de formação: "todo elemento da matriz A que for ímpar deve ser multiplicado por 2; caso contrário, o elemento da matriz A deve permanecer constante". Apresentar os elementos da matriz B.
#  Elaborar um programa que leia 15 elementos reais para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, observando a seguinte lei de formação: "todo elemento da matriz A que possuir índice par deve ter seu elemento dividido por 2; caso contrário, o elemento da matriz A deve ser multiplicado por 1.5". Apresentar os elementos da matriz B
A = []
B = []
for i in range(0, 12):
    A.append(int(input('Informe o {}° Valor de A: '.format(i + 1))))
for i in range(0, 12):
    if(A[i] % 2 == 0):
        B.append(A[i] / 2)
    else:
        B.append(A[i] * 1.5)
print('--------------------------------------------')
for i in range(0, 12):
    print('B[{}] = {}'.format(i + 1, B[i]))