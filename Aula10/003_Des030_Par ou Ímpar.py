#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n=int(input('Digite o número a ser verificado: '))
ver=n%2
if ver == 0:
  print('O número digitado foi {} que é PAR!'.format(n))
else:
  print('O número digitado for {} que é ÍMPAR!'.format(n))
print('Fim do Programa!')