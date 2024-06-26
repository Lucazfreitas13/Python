#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em ºC a ser convertida em fahrenheit: '))
convers = (celsius*1.8)+32
print('A temperatura {:.1f}ºC em Fahrenheit é {:.1f}ºF'.format(celsius, convers))

