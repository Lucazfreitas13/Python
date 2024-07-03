nota1=float(input('Informe a primeira nota: '))
nota2=float(input('Informe a segunda nota: '))
media=(nota1+nota2)/2
if media >= 7:
  print('Aprovado! Sua nota foi {:.1f}'.format(media))
elif media >= 5 and media < 7:
  print('Em Recuperação! Sua nota foi {:.1f}'.format(media))
elif media <5:
  print('Reprovado!')