#O mesmo professor do desafio anterior quer sortear a de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e montre a ordem sorteada.
import random
a1=str(input('Informe o nome do primeiro aluno: '))
a2=str(input('Informe o nome do segundo aluno: '))
a3=str(input('Informe o nome do terceiro aluno: '))
a4=str(input('Informe o nome do quarto aluno: '))
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
