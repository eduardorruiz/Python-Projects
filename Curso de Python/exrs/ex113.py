""" Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
 da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido')
            continue # joga pro laço denovo.
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número real válido')
            continue  # joga pro laço denovo.
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
n = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'Você acabou de digitar o número {n} e o real foi {n2}.')
