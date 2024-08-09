import os

idade = int(input('Digite a sua idade: '))
if 0 < idade <=12:
 print('Você é criança')
elif 12 < idade <18:
 print('Você é adolescente')
elif idade >=18:
 print('Você é adulto')
else:
 print('Idade inválida')