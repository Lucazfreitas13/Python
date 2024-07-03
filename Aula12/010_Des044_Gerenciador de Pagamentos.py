#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' SUA LOJA '))
p=float(input('Informe o valor do produto: R$ '))
desPagVist=int(input('Informe a % de desconto para pagamentos à vista no dinheiro/PIX: '))
DesCartVis=int(input('Informe a % de desconto para pagamento à vista no cartão: '))
jurosCart=int(input('Informe a % de Juros no pagamento a prazo: '))
print('TABELA DE COD DE PAGAMENTO')
c1=print('1 = À Vista DINHEIRO/PIX: {}% de desconto'.format(desPagVist))
c2=print('2 = À vista no CARTÃO: {}% de desconto'.format(DesCartVis))
c3=print('3 = Em até 2x no CARTÃO: Preço Normal')
c4=print('4 = 3x ou mais no CARTÃO: {}% de Juros'.format(jurosCart))
calcDesVis=desPagVist/100
calcCartVis=DesCartVis/100
calcJurosCart=jurosCart/100
tipoPagamento=int(input('Informe o código da condição de pagamento: '))
if tipoPagamento == 1:
  print('                   \033[0;30;42mPagamento à vista no Dinheiro/PIX\033[m                   ')
  print('Valor Original: R$ {:.2f}\nDesconto Aplicado: {}%\nValor de Desconto: R$ {:.2f}\nValor Final: R$ {:.2f}'.format(p,desPagVist,p*calcDesVis,p-(p*calcDesVis)))
elif tipoPagamento == 2:
  print('                   \033[0;30;42mPagamento à vista no Cartão\033[m                   ')
  print('Valor Original: R$ {:.2f}\nDesconto Aplicado: {}%\nValor de Desconto: R$ {:.2f}\nValor Final: R$ {:.2f}'.format(p,DesCartVis,p*calcCartVis,p-(p*calcCartVis)))
elif tipoPagamento == 3:
  print('                   \033[0;30;42mPagamento em 2x no Cartão\033[m                   ')
  print('Valor Final: R$ {:.2f}\nValor Parcelas: R$ {:.2f} Sem Juros'.format(p,p/2))
elif tipoPagamento == 4:
  print('                   \033[0;30;42mPagamento 3x ou mais no Cartão\033[m                   ')
  nParc=int(input('Informe a quantidade de parcelas do pagamento: '))
  print('Valor Original: R$ {:.2f}\nJuros aplicado: {}%\nValor de Juros: R$ {:.2f}\nValor Final: R$ {:.2f}\nValor Parcelas: R$ {:.2f}'.format(p,jurosCart,p*calcJurosCart,p+(p*calcJurosCart),(p+(p*calcJurosCart))/nParc))
else:
  print('\033[1;31mCódigo de Pagamento digitado Inválido!\033[m')
