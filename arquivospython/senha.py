import os

usuario_correto = 'Lucas'
senha_correta = '1234'

usuario_inserido = input('Digite seu usuário: ')
senha_inserida = input('Digite sua senha: ')

if usuario_inserido == usuario_correto and senha_inserida == senha_correta:
 print('Login bem sucedido')
else:
 print('Login inválido')