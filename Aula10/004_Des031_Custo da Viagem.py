#Desenvolva um programa que pergunte a distência de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.
km=float(input('Informe a distância em KM da sua viagem: '))
if km <= 200:
  print('Sua viagem de {}Km terá um custo de R$ 0,50 por Km, totalizando R$ {:.2f}'.format(km,km*0.50))
else:
  print('Sua viagem de {}Km terá um custo de R$ 0,45 por Km, totalizando R$ {:.2f}'.format(km,km*0.45))
print('Boa Viagem 🗺️')