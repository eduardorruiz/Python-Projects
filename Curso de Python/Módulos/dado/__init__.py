def leiadinheiro(mensagem):
    válido = False
    while not válido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO: "" é um preço inválido!')
        else:
            válido = True
            return float(entrada)

def leiaint(mensagem):
    n = input(mensagem).strip()
    while not n.isnumeric():
        print('ERRO, digite um número inteiro válido!')
        n = input(mensagem).strip()
    return int(n)

def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido')
            continue  # joga pro laço denovo.
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