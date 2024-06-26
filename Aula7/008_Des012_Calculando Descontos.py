#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:
p = float(input('Informe o valor total: R$ '))
desconto = float(input('Informe o % de desconto: '))
formDesc = desconto/100
print('Valor final com desconto de {:.2f}% = R$ {:.2f}'.format(desconto, p-(p*formDesc)))
print('Valor Original: R${:.2f}\nValor Final: R${:.2f}\nDesconto: R${:.2f}'.format(p, p-(p*formDesc), p-(p-(p*formDesc))))

#p*desconto/100