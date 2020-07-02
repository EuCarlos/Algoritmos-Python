# Elaborar um programa que leia 20 elementos (valores reais) para temperaturas em graus Celsius e armazene esses valores em uma matriz A de uma dimensão. O programa ao final deve apresentar a menor, a maior e a média das temperaturas lidas. 
A = []
S = 0
for i in range(0,5):
    A.append(float(input('Informe o {}° Valor em Graus Celsius do vetor A: '.format(i + 1)))
for i in range(0, 5):
    S = S + A[i]
VMaior = A[1]
VMenor = A[1]
for i in range(1, 5):
    if (VMaior > A[i]):
        VMaior = A[i]
    if (VMenor < A[i]):
        VMenor = A[i]
MediaFinal = S / 5
print('{}°C é o MAIOR valor informado, {}°C é o MENOR valor informado e {} é a MEDIA FINAL das temperaturas'.format(VMaior, VMenor, MediaFinal))