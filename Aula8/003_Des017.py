#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
a=float(input('Informe o comprimento do cateto oposto (a): '))
b=float(input('Informe o comprimento do cateto adjacente (b): '))
h=math.sqrt(math.pow(a,2)+math.pow(b,2))
#h=math.hypot(a,b)
print('A hipotenusa de A: {:.f2}cm e B: {:.2f}cm é C: {:.2f}cm'.format(a,b,h))