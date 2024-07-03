#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
import datetime
anoAtual=datetime.date.today().year
anoNasc=int(input('Informe o ano de nascimento do atleta: '))
idade=anoAtual-anoNasc
if idade <= 9:
  print('Idade do(a) Atleta {} - Categoria: MIRIM'.format(idade))
elif idade <= 14:
  print('Idade do(a) Atleta {} - Categoria: INFANTIL'.format(idade))
elif idade <= 19:
  print('Idade do(a) Atleta {} - Categoria: JÚNIOR'.format(idade))
elif idade <= 25:
  print('Idade do(a) Atleta {} - Categoria: SÊNIOR'.format(idade))
elif idade > 25:
  print('Idade do(a) Atleta {} - Categoria: MASTER'.format(idade))