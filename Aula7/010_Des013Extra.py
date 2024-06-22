p = float(input('Informe o valor original do produto: R$'))
pgVista = float(input('Informe o % de desconto no pagamento a vista:'))
pgPrazo = float(input('Informe o % de taxa da máquina de cartão:'))
calDesc = pgVista/100
calJuros = pgPrazo/100
pagamento = str(input('Informe se o pagamento foi a vista ou a prazo: '))
if pagamento in ['a vista', 'vista', 'VISTA', 'A VISTA', 'A vista', 'a Vista', 'a VISTA']:
    print('O pagamento será a vista com desconto de {:.2f}%.\nValor Original: R${:.2f}\nValor Final: R${:.2f}\nDesconto: R${:.2f}'.format(pgVista, p, p-(calDesc*p), (calDesc*p)))
else:
    print('O pagamento será a prazo, acarretando o acréscimo de {:.2f}% de juros.\nValor Original: R${:.2f}\nValor final: R${:.2f}\nJuros: R${:.2f}'.format(pgPrazo, p, p+(calJuros*p), (calJuros*p)))
