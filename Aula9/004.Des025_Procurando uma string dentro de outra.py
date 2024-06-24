#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome
nome=str(input('Informe o seu nome completo: ')).strip()
nomeAjus=nome.upper().split()
print('Existe a palavra "SILVA" no nome','SILVA' in nomeAjus)