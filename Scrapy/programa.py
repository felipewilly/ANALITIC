from front.interface import *
from back.dados import *

'''
Programa principal, com interação ao ususario via terminal.
Ordem de processo: 1° dados sofa score, 2° dados extraidos
'''
titulo('Programa Analitc') 
#Menu principal
while True:
    menu()
    esc = int(input('Opição: '))
    linha()
    if esc == 1:
        adiciona()
    if esc == 2: #Escolha do usuario que vai receber os dados pra retirada da media
        chama_dicionarios()
    if esc == 3:
        teste_funcional()
    if esc == 4:
        break
#Criando submenu
while True:
    submenu()
    esc = int(input('Opição: '))
    linha()
    if esc == 1:
        adiciona()
    if esc == 2:
        chama_dicionarios()
    if esc == 3:
        teste_funcional()
    if esc == 4:
        teste_automatizar()
    if esc == 5:
        break
