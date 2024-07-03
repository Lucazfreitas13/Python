#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
r1=float(input('Informe a medida da primeira reta: '))
r2=float(input('Informe a medida da segunda reta: '))
r3=float(input('Informe a medida da terceira reta: '))
if (r1+r2)>r3 and (r2+r3)>r1 and (r1+r3)>r2:
  print('As medidas informadas formam um triângulo ', end='')
  if r1 == r2 and r2 == r3:
    print('Equilátero!')
  elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Isósceles!')
  elif r1 != r2 and r2 != r3 and r3 != r1:
    print('Escaleno!')
else:
  print('As médidas informadas não formam um triângulo!')