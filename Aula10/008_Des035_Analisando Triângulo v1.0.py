#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se las podem ou não formar um triângulo:
r1=float(input('Digite a medida da primeira reta: '))
r2=float(input('Digite a medida da segunda reta: '))
r3=float(input('Digite a medida da terceira reta: '))

if (r1+r2)>r3 and (r1+r3)>r2 and (r3+r2)>r1:
  print('As medidas informadas formam um triângulo!')
else:
  print('As medidas informadas não formam um triângulo!')
