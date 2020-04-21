# Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores após a efetivação do processamento da troca.
A = input('valor de A: ')
B = input('Valor de B: ') 
Aux = B
B = A
A = Aux
print(' Valor de A: {} \n Valor de B: {}'.format(A , B))