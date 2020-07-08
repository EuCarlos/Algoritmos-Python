#  Elaborar um programa que leia oito elementos numéricos inteiros em uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesma dimensão e tipo com os elementos da matriz A multiplicados por 5. Montar uma rotina de pesquisa binária, para pesquisar os elementos armazenados na matriz B. 
A = []
B = []
for i in range(0, 8):
    A.append(int(input('Informe {}° valor de A: '.format(i + 1))))
for i in range(0, 8):
    B.append(A[i] * 5)
# Pesquisa Binaria
for i in range(0, 7):
    for j in range(0, 8):
        if(B[i] > B[j]):
            X = B[i]
            B[i] = B[j]
            B[j] = X
R = "SIM"
while(R == "SIM"):
    Pesq = input('Pesquisa: ')
    Com = 1
    Fin = 8
    Ach = False
    while(Com <= Fin) and (Ach == False):
        Mei = (Con + Fin) / 2
        if(Pesq == B[Mei]):
            Ach = True
        else:
            if(Pesq < B[Mei]):
                Fin = Mei - 1
            else:
                Fin = Mei + 1
    if(Ach == True):
        print('{} foi localizado na posição {}'.format(Pesq, Mei))
    else:
        print('{} não foi localizado'.format(Pesq))
    R = input('R: ')