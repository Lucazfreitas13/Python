#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opc=int(input('Digite a opção desejada: '))
if opc == 1:
  print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opc == 2:
  print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opc == 3:
  print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
  print('\033[1;31mOpção digitada é inválida!\033[m')

