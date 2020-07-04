#  Elaborar um programa que leia uma matriz A de uma dimensão com dez elementos numéricos inteiros. Apresentar o total de elementos ímpares existentes na matriz e também o percentual do valor total de números ímpares em relação à quantidade total de elementos armazenados na matriz
A = []
Impar = 0
for i in range(0, 10):
    A.append(int(input('Informe o {}° valor de A: '.format(i +1))))
    if(A[i] % 2 == 1):
        Impar = Impar + 1
Perc = Impar / 10 * 100
print('--------------------------------------------------------------------------')
print('O total de numeros IMPARES informados é igual a {} com Percentual de {}%'.format(Impar, Perc))