#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome=str(input('Digite seu nome completo: ')).strip()
n=nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[-1]))

#[-1] representa o último elemento da lista, que no seu exemplo seria o 'e'. Assim como o [-2] seria o penúltimo, o [-3] seria o antecessor do [-2]....