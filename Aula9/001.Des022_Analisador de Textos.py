#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúculas
#Quantas letras ao todo(Sem Considerar espaços)
#Quantas letras tem o primeiro nome.
nome=str(input('Informe seu nome completo: ')).strip()
print('Nome Maiúsculo: ',nome.upper())
print('Nome Minúsculo: ',nome.lower())
Div=nome.split()
print('Seu nome completo possui {} letras'.format(len(''.join(Div))))
#print('Seu nome completo possui {} letras'.format(len(nome)-nome.count(' ')))
print('Quantos caracteres tem o nome completo: ',len(nome))
print('Quantas letras tem o Primeiro Nome: ',len(Div[0]))


