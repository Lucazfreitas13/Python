#Escreva um program aque leia a velocidade de um carro: Se ele ultrapassar 80km/h. Mostre um mensagem que ele foi multado. A multa vai custa R$ 7,00 por cada KM acima do limite.

velocidade=float(input('Velocidade do carro: '))
multa=(velocidade-80)*7
if velocidade >80:
  print('❗Você foi multado em R${:.2f}, devido ter ultrapassado no radar a {} Km/h. Onde o limite é 80 Km/h ❗'.format(multa,velocidade))
