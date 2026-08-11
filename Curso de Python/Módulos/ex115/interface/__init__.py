def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido\033[m')
            continue  # joga pro laço denovo.
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('\033[1mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - {item}')
        c += 1
    print(linha())
    opção = leiaInt('\033[4mSua Opção:\033[m ')
    return opção