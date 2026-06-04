# Eduardo Rocha Ruiz, Flávio Filho, Geovanna Serafim e Sofia Escalassara.

from random import choice
def GeraSenha(tipo_de_senha, tamanho_da_senha):
    if tipo_de_senha == 'A':
        caracteres = '0123456789'
    elif tipo_de_senha == 'B':
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif tipo_de_senha == 'C':
        caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    elif tipo_de_senha == 'D':
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    elif tipo_de_senha == 'E':
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_!?#@*&=$%'
    senha = ''
    for _ in range(tamanho_da_senha):
        senha += choice(caracteres)
    return senha

# Programa Principal
tipo_de_senha = input('Digite o tipo de senha: ').strip().upper()[0]
while tipo_de_senha not in 'ABCDE':
    print('Tipo de senha inválido')
    tipo_de_senha = input('Digite o tipo de senha, novamente: ').strip().upper()[0]
tamanho_da_senha = int(input('Digite a tamanho da senha: '))
while tamanho_da_senha < 6 or tamanho_da_senha > 25:
    print('O tamanho da senha não pode ser inferior a 6 nem maior que 25 caracteres')
    tamanho_da_senha = int(input('Digite a tamanho da senha, novamente: '))
entrada = open('MATR.TXT', 'r')
saida = open('SENHAS.TXT', 'w')
matriculas = []
for linha in entrada:
    matriculas.append(linha)
entrada.close()
for matricula in matriculas:
    matricula = matricula.strip()
    senha = GeraSenha(tipo_de_senha, tamanho_da_senha)
    saida.write(f'{matricula};{senha};\n')
saida.close()