#  Elaborar um programa que leia 12 elementos inteiros para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmo tipo e dimensão, observando a seguinte lei de formação: "todo elemento da matriz A que for ímpar deve ser multiplicado por 2; caso contrário, o elemento da matriz A deve permanecer constante". Apresentar os elementos da matriz B.
A = []
B = []
for i in range(0, 12):
    A.append(int(input('Informe o {}° Valor de A: '.format(i + 1))))
for i in range(0, 12):
    if(A[i] % 2 == 1):
        B.append(A[i] * 2)
    else:
        B.append(A[i])
print('--------------------------------------------')
for i in range(0, 12):
    print('B[{}] = {}'.format(i + 1, B[i]))