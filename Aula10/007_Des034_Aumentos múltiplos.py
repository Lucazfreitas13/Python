#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal=float(input('Informe o salário atual do colaborador: R$'))
if sal>1250:
  print('O reajuste salarial foi de 10%.\nNova Remuneração: R${:.2f}'.format((sal*0.10)+sal))
else:
  print('O reajuste salarial foi de 15%.\nNova Remuneração: R${:.2f}'.format((sal*0.15)+sal))