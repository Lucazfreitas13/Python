#Um Professor quer sortear um dos seus quatros alunos para apgar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
a1=str(input('Informe o nome do primeiro aluno: '))
a2=str(input('Informe o nome do segundo aluno: '))
a3=str(input('Informe o nome do terceiro aluno: '))
a4=str(input('Informe o nome do quarto aluno: '))
lista = [a1,a2,a3,a4]
from random import choice
sort=choice(lista)
print('🤓 O aluno escolhido foi:🤓{}🤓'.format(sort))