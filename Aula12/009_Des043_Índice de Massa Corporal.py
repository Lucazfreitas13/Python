#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('                   Calculadora IMC                   ')
peso=float(input('Informe seu Peso (Kg): '))
altura=float(input('Informe sua altura (m): '))
imc=peso/pow(altura,2)
cores={'verde':'\033[1;30;42m',
      'vermelho':'\033[1;30;41m',
      'amarelo':'\033[1;30;43m',
      'limpar':'\033[m'}
if imc >= 40:
  print('IMC: {:.1f} - Status:{} Obesidade Mórbida {}'.format(imc,cores['vermelho'],cores['limpar']))
elif imc >=30 and imc <40:
  print('IMC: {:.1f} - Status:{} Obesidade {}'.format(imc,cores['vermelho'],cores['limpar']))
elif imc >=25 and imc <30:
  print('IMC: {:.1f} - Status:{} Sobrepeso {}'.format(imc,cores['amarelo'],cores['limpar']))
elif imc >=18.5 and imc <25:
  print('IMC: {:.1f} - Status:{} Peso Ideal {}'.format(imc,cores['verde'],cores['limpar']))
else:
  print('IMC: {:.1f} - Status:{} Abaixo do Peso {}'.format(imc,cores['amarelo'],cores['limpar']))
