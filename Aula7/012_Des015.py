#Escreva um progrma que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

d=int(input('Informe a quantidade de dias de aluguel do carro: '))
km=float(input('Informe a quantidade de Km rodados durante o aluguel: '))
vDiaria=float(input('Valor da diária do aluguel: R$ '))
vKm=float(input('Valor por Km rodado: R$ '))
custoDiaria=d*vDiaria
custoKm=km*vKm
print('Segue abaixo o demostrativo de valores a serem pagos referente ao aluguel do veículo:')
print('Custo diária: R$ {:.2f}\nCusto KMs: R$ {:.2f}\nTotal a Pagar: R$ {:.2f}'.format(custoDiaria,custoKm,custoKm+custoDiaria))
print(90*'-')
print('Obrigado por utilizar nossos serviços, volte sempre!')
