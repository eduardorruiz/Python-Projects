''' Para todos os exercícios acima, faça com que a saída, além de ser exibida na tela, também seja gravada
em um arquivo texto em disco. '''

arq = open('saidaprpgramas.txt', 'w')
arq.write(f'{O resultado}\n')
arq.close()