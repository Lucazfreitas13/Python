#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('                   \033[1;97;41m Simulador de Empréstimo de Imóvel \033[m                   ')
valorImovel=float(input('Informe o valor total do imóvel: R$ '))
salario=float(input('Informe o salário do cliente: R$ '))
anos=int(input('Informe quantidade de anos do empréstimo: '))
valorPrestacao=float(valorImovel/(anos*12))
qntParcelas=(anos*12)
limiteSalario=salario*0.30
if valorPrestacao > limiteSalario:
  print('\033[1;31;107mEmpréstimo recusado devido as condições financeiras não atenderem os requísitos mínimos!\033[m')
elif valorPrestacao <= limiteSalario:
  print('\033[1;32;107mParabéns, Empréstimo aprovado!\033[m')
  print('                   Condições do Empréstimo:                   \nValor do Imóvel: R$ {:.2f}\nParcelas: {}\nValor Parcela: R$ {:.2f}'.format(valorImovel,qntParcelas,valorPrestacao))
print('                   💰Banco Nacional agradece a preferência!💰                   ')
