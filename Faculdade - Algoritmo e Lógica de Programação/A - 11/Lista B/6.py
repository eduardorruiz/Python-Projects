""" Desenvolva um jogo da forca. O programa deve iniciar lendo uma palavra digitada pelo preparador do jogo.
Outro jogador terá que adivinhar essa palavra. Para isso ele pode digitar uma letra ou a palavra toda.
Se digitar uma letra ela será considerada uma sugestão. Se a sugestão estiver correta as letras serão exibidas à
medida que o jogador acertar. O jogador poderá errar 6 letras antes de ser enforcado.
Se o jogador souber a resposta deve escrever a palavra completa. Neste caso, ele pode acertar e vencer ou se
errar morre imediatamente. Para jogar considerem que apenas letras maiúsculas serão usadas.
Desafio: Prepare um arquivo com uma palavra em cada linha. Leia esse arquivo carregando as palavras em uma
lista e no início do jogo sorteie uma das palavras da lista. """
""" A palavra é: _ _ _ _ _ _
Digite uma letra ou a palavra: A
-> Você errou pela 1ª vez. Tente de novo!
Digite uma letra ou a palavra: O
A palavra é: _ O _ _ _ O
Digite uma letra ou a palavra: E
A palavra é: _ O E _ _ O
Digite uma letra ou a palavra: S
-> Você errou pela 2ª vez. Tente de novo!
Digite uma letra ou a palavra: C
A palavra é: C O E _ _ O
Digite uma letra ou a palavra: COELHO
-> !!! Você ACERTOU “O” !!!
Se o jogador errar então o texto será
-> Xiiiii... MORREUUUUU... """