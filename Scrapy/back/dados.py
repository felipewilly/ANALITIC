from front.interface import *
import os
'''
Dentro deste modulo esta toda as funções resposaveis por tratar
e executar todos os dados, segiunte ordem de processo esta ABRE_L, pra receber o time
e o link da partida do usuario.

ADICIONA, recebe dados manuais de outros site.
'''
def erros(esc):
    '''
    Função desativada temporariamente até entrar em produção.
    '''
    while True:    
        try:
            nome = str(input(esc))
        except(TypeError, ValueError):
            print('\nSua tentativa deu algo errado')
            continue
        except(KeyboardInterrupt):
            print('Encerrado pelo usuario')
            return 0
        else:
            return nome

def abre_l(url, time):
    #temporario aguarda biblioteca scrapy pra recber url
    global partida
    partida = {'link':url, 'campo':time}
    #aguardar  a analise de como scrapy vai receber daqui
    return partida

def retorno_url():
    return partida

def chamda_scrapi():
    '''
    Função pra chamar uma biblioteca externa devido ao uso do CMD.
    '''
    os.system('cd C:/Users/Felip/Documents/ANALITIC/Scrapy/aiscore/aiscore/spiders & scrapy crawl airscore -O airscore.json ')

def adiciona(povo, robo):
    '''
    Função pra somar os dados recebido e formatado.
    '''
    soma = povo + robo
    return soma

def verifica(teste):
    '''
    Função desativada temporariamente até pois vai verificar existencia de arquivos
    '''
    try:
        teste = open('aiscore.json', 'rt')
        teste.close()
    except(FileNotFoundError, FileExistsError):
        return False
    else:
        return True
        

            
            