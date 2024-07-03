#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
anoAtual=datetime.date.today().year
anoNas=int(input('Informe o seu ano de nascimento:'))
print('''     Códigos de Sexo
      [1] Masculino
      [2] Feminino''')
sexo=int(input('Informe o código do seu sexo, conforme tabela acima: '))
idade=anoAtual-anoNas
if sexo == 2:
  print('O alistamento não é obrigatório para o sexo feminino!')
elif sexo == 1:
  if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNas,idade,anoAtual))
    print('Você precisa se alistar nesse ano, não perca o prazo!')
  elif idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNas,idade,anoAtual))
    print('Você ainda não tem idade suficiente para se alistar. \033[1mO alistamento precisa acontecer no ano que você completa 18 anos!\033[m')
    print('\033[1,32mFalta {} anos para seu alistamento!\033[m'.format(18-idade))
    print('Seu alistamento será em {}'.format(anoAtual+(18-idade)))
  elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNas,idade,anoAtual))
    print('Você deveria ter se alistado há {} anos! \033[1;31mProcure o exército da sua cidade imediatamente!\033[m'.format(idade-18))
    print('O ano do ser alistamento foi em {}'.format(anoAtual-(idade-18)))
else:
  print('\033[1;31mCódigo digitado incorreto! Tente Novamente!\033[m')


