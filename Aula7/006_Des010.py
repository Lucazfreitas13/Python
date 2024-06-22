#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e montre quantos dólares ela pode comprar.

carteira=float(input('Dígite o total em R$ que possuí para conversão: R$ '))
dolar=float(input('Digite a contação do dólar/real: '))
conversao=carteira/dolar
print('Com a cotação atual é possível com o total de R$ {:.2f} adquirir o total de US$ {:.2f}'.format(carteira,conversao))