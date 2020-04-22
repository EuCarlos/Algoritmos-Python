# Elaborar um programa que leia uma medida em pés e apresente o seu valor convertido em metros, lembrando que um pé mede 0,3048 metro, ou seja, um pé é igual a 30,48 centímetros. 
P = float(input('informe o valor em pés: '))
Mt = P * 0.3048
print('{} pés é equivalente a {} metros'.format(P, Mt))