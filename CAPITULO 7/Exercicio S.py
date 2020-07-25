# Elaborar um programa que leia dez elementos numéricos reais em uma matriz A do tipo vetor e apresente esses elementos por meio de pesquisa sequencial.
A = []
for i in range(10):
    A.append(float(input('Informe um elemento para a matriz A[{}]: '.format(i))))

R = "SIM"
while(R == "SIM"):
    Pesq = float(input('Pesquisa'))
    i = 1
    Acha = False
    while((i <= 10) and (Acha ==  False)):
        if(Pesq == A[i]):
            Acha = True
        else:
            i += 1
    if(Acha == True):
        print('{} foi localizado na posição {}'.format(Pesq, i))
    else:
        print('{} não foi encontrado.'.format(Pesq))
    R = input('RESPOSTA: ')
