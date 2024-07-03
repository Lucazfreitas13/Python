#Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time
cores={
  'limpa':'\033[m',
  'verde':'\033[1;32m',
  'vermelho':'\033[1;31m',
  'amerelo':'\033[1;33m',}
print('                   \033[1;33;107m Jogo Jokenpô \033[m                   ')
print('Tabela de codigo selecionáveis')
print('1= 🖐️\n2= ✌️\n3= 👊')
papel1='🖐️'
tesoura2='✌️'
pedra3='👊'
jogador=int(input('Informe o código se acordo com a tabela acima: '))
while jogador != 1 and jogador != 2 and jogador != 3:
    print('{}Opção Digitada inválida. Tente Novamente!{}'.format(cores['vermelho'],cores['limpa']))
    jogador=int(input('Informe o código se acordo com a tabela acima: '))
else:
  if jogador == 1:
    opcaoJogador='🖐️'
  elif jogador == 2:
    opcaoJogador='✌️'
  elif jogador == 3:
    opcaoJogador ='👊'
opcoesJogo=[papel1,tesoura2,pedra3]
pc=random.choice(opcoesJogo)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=-'*17)
print('{}Jogador ={} {} X {}PC ={} {}'.format(cores['verde'],opcaoJogador,cores['limpa'],cores['vermelho'],pc,cores['limpa']))
print('-=-'*17)
while opcaoJogador == pc:
  print('{}  X {} = {}Empate!{}'.format(opcaoJogador,pc,cores['amerelo'],cores['limpa']))
  print('{}Jogue Novamente!{}'.format(cores['verde'],cores['limpa']))
  print('Tabela de codigo selecionáveis')
  print('1= 🖐️\n2= ✌️\n3= 👊')
  jogador=int(input('Informe o código se acordo com a tabela acima: '))
  while jogador != 1 and jogador != 2 and jogador != 3:
    print('{}Opção Digitada inválida. Tente novamente!{}'.format(cores['vermelho'],cores['limpa']))
    jogador=int(input('Informe o código se acordo com a tabela acima: '))
  else:
    if jogador == 1:
      opcaoJogador='🖐️'
    elif jogador == 2:
      opcaoJogador='✌️'
    elif jogador == 3:
      opcaoJogador ='👊'
  opcoesJogo=[papel1,tesoura2,pedra3]
  pc=random.choice(opcoesJogo)
  print('JO')
  time.sleep(1)
  print('KEN')
  time.sleep(1)
  print('PO!!!')
  print('-=-'*17)
  print('{}Jogador ={} {} X {}PC ={} {}'.format(cores['verde'],cores['limpa'],opcaoJogador,cores['vermelho'],cores['limpa'],pc))
  print('-=-'*17)
else:
  if opcaoJogador =='🖐️' and pc == '✌️':
    print('{}  X {} = {}Você Perdeu!{}'.format(opcaoJogador,pc,cores['vermelho'],cores['limpa']))
  elif opcaoJogador == '🖐️' and pc == '👊':
    print('{}  X {} = {}Você Ganhou!{}'.format(opcaoJogador,pc,cores['verde'],cores['limpa']))
  elif opcaoJogador == '👊' and pc == '🖐️':
    print('{}  X {} = {}Você Perdeu!{}'.format(opcaoJogador,pc,cores['vermelho'],cores['limpa']))
  elif opcaoJogador == '👊' and pc == '✌️':
    print('{}  X {} = {}Você Ganhou!{}'.format(opcaoJogador,pc,cores['verde'],cores['limpa']))
  elif opcaoJogador == '✌️' and pc == '🖐️':
    print('{}  X {} = {}Você Ganhou!{}'.format(opcaoJogador,pc,cores['verde'],cores['limpa']))
  elif opcaoJogador == '✌️' and pc == '👊':
    print('{}  X {} = {}Você Perdeu!{}'.format(opcaoJogador,pc,cores['vermelho'],cores['limpa']))
