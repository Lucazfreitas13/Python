#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
n=float(input('Inform um número real: '))
inte=math.trunc(n)
print('O número digitado foi {} e sua porção inteira é {}'.format(n,inte))
