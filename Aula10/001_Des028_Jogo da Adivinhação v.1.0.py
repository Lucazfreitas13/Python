#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
from random import randint
jogoPc=randint(0,5)
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar....')
print('-=-'*25)
jogador=int(input('Digite o número sorteado pelo computador: '))
print('⏳Analizando sua resposta. Aguarde!⏳')
time.sleep(2)
if jogoPc == jogador:
  print('🤑 Você acertou! O número sorteado foi {}'.format(jogoPc))
else:
  print('🥺 Você errou! o número escolhido pela máquina foi {}'.format(jogoPc))
  print('Tente Novamente!😉')
print('-=-'*25)  
print('Fim do Jogo!')
