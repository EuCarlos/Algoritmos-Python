# Em uma eleição sindical concorreram ao cargo de presidente três candidatos (representados pelas variáveis A, B e C). Durante a apuração dos votos foram computados votos nulos e em branco, além dos votos válidos para cada candidato. Deve ser criado um programa de computador que faça a leitura da quantidade de votos válidos para cada candidato, além de também ler a quantidade de votos nulos e em branco. Ao final o programa deve apresentar o número total de eleitores, considerando votos válidos, nulos e em branco; o percentual correspondente de votos válidos em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato A em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato B em relação à quantidade de eleitores; o percentual correspondente de votos válidos do candidato C em relação à quantidade de eleitores; o percentual correspondente de votos nulos em relação à quantidade de eleitores; e por último o percentual correspondente de votos em branco em relação à quantidade de eleitores. 
A = int(input('Votos do Candidato A: '))
B = int(input('Votos do Candidato B: '))
C = int(input('Votos do Candidato C: '))
Nulo = int(input('Votos Nulos: '))
Branco = int(input('Votos em Branco: '))
TotE = A + B + C + Nulo + Branco
PorcVV = (A + B + C)* 100 / TotE
PorcN = Nulo * 100 / TotE
PorcB = Branco * 100 / TotE
print('===================================================')
print(' Total de Eleitores: {} \n Percentual de Votos Validos: {} \n Percentual de Votos Nulos: {} \n Percentual de Brancos {}'.format(TotE, PorcVV, PorcN, PorcB))