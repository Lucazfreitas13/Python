#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo.
import math
a=float(input('Informe o ângulo a sem calculado: '))
radiano=math.radians(a)
s=math.sin(radiano)
c=math.cos(radiano)
t=math.tan(radiano)
print('O angulo informado foi {}º\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(a,s,c,t))

