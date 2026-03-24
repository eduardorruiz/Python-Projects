# \033[style;text;backm
# style: 0=none(nada); 1 = Bold(Negrito); 4 = underline(sublinhado); 7 = negative(inverter as configs)
# text: 30 = branco; 31 = verm; 32 = verde; 33 = yellow; 34 = blue; 35 = purple; 36 = baby blue; 37 = cinza
# back: 40 = branco; 41 = verm; 42 = verde; 43 = yellow; 44 = blue; 45 = purple; 46 = baby blue; 47 = cinza
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m # sem o primeiro pq não tem estilo
\033[m #background preto e letra cinza = config padrão
\033[7;30m #inverteu pra ficar preto a letra e o fundo branco
# print('\033[...mOlá, mundo!')
# print('\033[...mOlá, mundo!\033[m') = com o \033[m no final, as configs acabam onde acabar o texto

# OU

# print('Olá , {}{}{} muito prazer!!'.format('\033[1;35m, nome, '\033[m'))