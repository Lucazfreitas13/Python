#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada:
n=int(input('Digite um número: '))
d=n*2
t=n*3
r=n**(1/2) #pow(n,(1/2))
print('O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raíz quadrada é {:.2f}'.format(n,d,t,r))
