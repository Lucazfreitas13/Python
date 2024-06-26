#Escreva um programa que leia um valor em metros e ao exiba convertido em centímetros e milímetros:

m=float(input('Digite o valor em metros a ser convertido: '))
dc=m*10
c=m*100
mm=m*1000
dam=m/10
hm=m/100
km=m/1000

print('O valor digitado foi {}m.\nConversão \nDecímetros: {:.0f}dm\nCentímetros: {:.0f}cm \nMelímetros: {:.0f}mm\nDecâmetros: {}dam\nHectômetros: {}hm\nQuilômetros: {}km'.format(m,dc,c,mm,dam,hm,km))