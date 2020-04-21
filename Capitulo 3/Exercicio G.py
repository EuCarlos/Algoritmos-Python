# Ler quatro valores numéricos inteiros e apresentar o resultado das adições e das multiplicações utilizando o mesmo raciocínio aplicado quando do uso de propriedades distributivas para a máxima combinação possível entre as quatro variáveis. Não é para calcular a propriedade distributiva, apenas para usar a sua forma de combinação. Considerando a leitura de valores para as variáveis A, B, C e D, devem ser feitas seis adições e seis multiplicações, ou seja, deve ser combinada a variável A com a variável B, a variável A com a variável C, a variável A com a variável D. Depois é necessário combinar a variável B com a variável C e a variável B com a variável D e, por fim, a variável C será combinada com a variável D
A = int(input('informe o valor A: '))
B = int(input('informe o valor B: '))
C = int(input('informe o valor C: '))
D = int(input('informe o valor D: '))
# Adição
soma1 = A + B 
soma2 = A + C
soma3 = A + D
soma4 = B + C
soma5 = B + D
soma6 = C + D
print('Somas:')
print(' 1° soma: {} \n 2° soma: {}\n 3° soma: {} \n 4° soma: {}\n 5° soma: {} \n 6° soma: {}'.format(soma1, soma2, soma3, soma4, soma5, soma6))
# Multiplicação
mult1 = A * B 
mult2 = A * C
mult3 = A * D
mult4 = B * C
mult5 = B * D
mult6 = C * D
print('Multiplicações:')
print(' 1° mult: {} \n 2° mult: {}\n 3° mult: {} \n 4° mult: {}\n 5° mult: {} \n 6° mult: {}'.format(mult1, mult2, mult3, mult4, mult5, mult6))