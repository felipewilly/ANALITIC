from front.interface import *
from back.dados import *

'''
Programa principal, com interação ao ususario via terminal.
'''

titulo('Programa Analitc') 
while True:
    menu()
    esc = input('Opção: ')
    if esc == '1':
        url = input(str('URL: '))
        time = input(str('Time analize [A] ou [B]: ')) #Escolha do usuario que vai mudar la no scrapy
        abre_l(url, time)
        chamda_scrapi()

    if esc == '2': #Escolha do usuario que vai receber os dados pra retirada da media
       povo  = int(input('Voto povo: ', ))
       robo = int(input('Robo Sofa: '))
       resultado = adiciona(povo, robo)

    if esc == '3':
        print(retorno_url)

    if esc == '4':
        break