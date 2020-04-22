# Elaborar um programa de computador que calcule e apresente o valor do volume de uma esfera. Utilize a fórmula VOLUME <- (4 / 3) * 3.14159 * (RAIO ^ 3).
R = float(input('informe o valor do Raio da esfera: '))
vol = (4 / 3) * 3.14159 * (R ** 3)
print('Volume da Esfera é igual a {}'.format(vol))