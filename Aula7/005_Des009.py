#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#n=int(input('Dígite o número para visualizar sua tabuada: '))
#t0=n*0
#t1=n*1
#t2=n*2
#t3=n*3
#t4=n*4
#t5=n*5
#t6=n*6
#t7=n*7
#t8=n*8
#t9=n*9
#t10=n*10
#print('Tabuada do {}\n{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n,n,t0,n,t1,n,t2,n,t3,n,t4,n,t5,n,t6,n,t7,n,t8,n,t9,n,t10))

n=int(input('Dígite o número para visualizar sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(n,0,n*0))
print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {:2} = {}'.format(n,5,n*5))
print('{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {:2} = {}'.format(n,10,n*10))
print('-'*12)