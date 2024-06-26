#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s=float(input('Informe o salário atual: R$ '))
reajuste=float(input('Informe o % de aumento: '))
calReaj=reajuste/100
print('Informamos que você recebeu um mérito de {:.2f}% devido ao seu desempenho em nossa organização.\nNova remuneração: R$ {:.2f}'.format(reajuste,s+(s*calReaj)))
print('Parabéns :)')