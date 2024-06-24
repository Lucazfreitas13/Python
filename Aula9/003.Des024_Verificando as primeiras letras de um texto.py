#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
cidade=str(input('Digíte o nome da sua cidade: ')).strip()
divCidade=cidade.upper().split()
print('O nome da cidade começa com a palavra "santo"?: ',divCidade[0]=='SANTO')
