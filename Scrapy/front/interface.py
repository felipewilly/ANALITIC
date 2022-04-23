"""
Neste aquivo temos a parte de animação, e efeitos visuais via terminal
"""
import json


c = (
    '\033[0;0m',  #cor reset 0
    '\033[1;31m', #Cor vermelho 1
    '\033[1;32m', #Cor verde 2
    '\033[1;101m',#Cor com fundo Vermelho Claro 3
    '\033[1;44m', #Cor com fundo Azul 4
    '\033[1;33m'  #Cor com amarelo  5
) #Variavel pra armazenar somente cores.

def titulo(mens):
    print(linha())
    print(mens.center(30))
    print(linha())

def linha(tam = 30):
    return '-' * tam

def menu():
    lista = ['Adicionar dados SOFA e URL', 'Adcionar URL', 'Testes Funcional', 'Ir Menu Partida.']
    cont = 0
    for item in lista:
        cont = cont + 1
        print(f'\033[1;36m[{cont}]\033[0;0m - \033[1;33m{item}\033[0;0m')
    print(linha())

def submenu():
    print(linha())
    titulo('PARTIDA EM EXEC')
    lista = ['Adiciona Novo SOFA ', 'Ver dados ATUAL', 'Recarregar', 'Teste funcional', 'SAIR']
    cont = 0
    for item in lista:
        cont = cont + 1
        print(f'\033[1;44m[{cont}]\033[0;0m - \033[1;33m{item}\033[0;0m')
    print(linha())

def ver_dados():
    titulo('Dados da Partida atual')
    with open('dd.json', 'r') as file:
        dados = json.load(file)
        for k, c in dados[0].items():
            print(f'{k} = {c}')