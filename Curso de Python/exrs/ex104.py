""" Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘) """

def leiaint(mensagem):
    n = input(mensagem).strip()
    while not n.isnumeric():
        print('ERRO, digite um número inteiro válido!')
        n = input(mensagem).strip()
    return int(n)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

# Tava dando erro esse de baixo:

"""def leiaint(mensagem):
    while not(mensagem.isnumeric()):
        print('ERRO, digite um número inteiro valido!')
        mensagem = str(input('Digite um número: ')).strip()
    if mensagem.isnumeric():
        mensagem = int(mensagem)
        return mensagem
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')"""