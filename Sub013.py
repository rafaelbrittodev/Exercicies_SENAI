#Gerador de Senhas
#Solicite ao usuário o comprimento desejado da senha e gere uma senha aleatória desse tamanho.
import random
import string
from random import choice

x = int(input('Digite a quantidade de caracteres desejados para a geração de senha: '))

def random_pass(a):
    tamanho = a
    caracteres = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    senha = ''
    for i in range(a):
        senha += choice(caracteres)
    print('A senha de segurança gerada foi: ')
    print(f'\n{senha}')

random_pass(x)