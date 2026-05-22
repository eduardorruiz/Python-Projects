def CalcDV(entrada):
    i = soma = 0
    peso = 6
    divisor = 10000
    while entrada > 0:
        valor = entrada // divisor  # para pegar o valor + significativo
        soma += valor * peso
        entrada = entrada % divisor
        divisor = divisor // 10
        peso -= 1
    return soma % 7

#arqSai = open('saídaprog2.txt', 'w')
código = int(input('Digite o código: '))
while código > 0:
    if 10000 <= código and código <= 30000:
        dv = CalcDV(código)
        print(f' O DV de {código} é {dv}')
        #arqSai.write(f' {código}-{dv}\n')
    else:
        print(f'...{código} inválido')
    código = int(input('Digite o código: '))
#arqSai.close()
# As linhas com # são pra gravar o arquivo das resposta