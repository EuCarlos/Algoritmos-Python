# Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C = ((F - 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.  
F = int(input('Informe o valor de em °F: '))
C = ((F - 32) * 5)/9
print('{}°F é equivalente a {}°C'.format(F , C))