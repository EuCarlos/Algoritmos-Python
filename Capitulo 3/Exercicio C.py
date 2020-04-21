# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME <- 3.14159 *R^2 * ALTURA.  
Alt = float(input('Informe a altura da lata: '))
R = float(input('informe o raio da lata: '))
volume = 3.14159 * R**2 * Alt
print('O volume da lata corresponde a: {}'.format(volume))