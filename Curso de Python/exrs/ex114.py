"""Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com')
except urllib.error.URLError:
    print('O site PUDIM não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
