#Modulo de login
from datetime import datetime
import random
print('----------------------------------------------------------')
print('Registro de funcionários da empresa.')
print('----------------------------------------------------------')

nome = input('Digite seu nome: \n')
idade= int(input('Digite sua idade: \n'))

data_nasc = datetime.strptime(input('Digite sua data de nascimento dia/mês/ano: \n'), '%d/%m/%Y')
data_cadastro = datetime.now()

cartoes = ['R$50,00','R$250,00','R$120,00']

print('----------------------------------------------------------')
print(f'funcionario: {nome} \nidade: {idade} \ndata de nascimento {data_nasc}')
print('----------------------------------------------------------')


print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.')

print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}!!')
print('----------------------------------------------------------')
