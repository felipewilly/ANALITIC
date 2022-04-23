from time import sleep
from front.interface import *
import os
import json
'''
Dentro deste modulo esta toda as funções resposaveis por tratar
e executar todos os dados, segiunte ordem de processo esta ABRE_L, pra receber o time
e o link da partida do usuario.

ADICIONA, recebe dados manuais de outros site.
'''
def erros(esc): # desativada para execução 
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

def set_scrapy(): #tranferido para adiciona
    '''
    Função verifica dados link.. fazer tratamento de erro
    Chamada lá no modulo aiscore
    '''
    partida = {}
    partida['link'] = input(str('Url:'))
    partida['campo'] = input(str('Casa[A] ou Visitante[B]: '))
    return partida
  
def chamda_scrapi():
    '''
    Função pra chamar uma biblioteca externa devido ao uso do CMD.
    Definir uma forma de atualizar automatico a cada 30 segundos
    '''
    os.system('scrapy crawl airscore -O airscore.json --nolog')
    
def verifica(teste):#Desativado para fins de teste
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

def adiciona():
    '''
    Função pra somar os dados recebido e formatado.
    '''
    partida = {}
    partida['povo'] = int(input('Dados do Povo: '))
    partida['robo'] = int(input('Dados do Robo: '))
    partida['link'] = input(str('Url:'))
    partida['campo'] = input(str('Casa[A] ou Visitante[B]: '))
    with open('partida.json', 'w') as file:
        json.dump(partida, file)
    chamda_scrapi()
    return dados_time(partida['povo'], partida['robo'])

def dados_time(povo, robo):
    with open('airscore.json', 'r') as file:
        dd = json.load(file)
        soma = (povo + robo + dd[0]['Posse'] + dd[0]['Ataque']) / 4
        dd[0]['Povo'] = povo
        dd[0]['Robo'] = robo
        dd[0]['Media'] = soma
        with open('dd.json', 'w') as file:
            json.dump(dd, file)
        if soma < 51:
            print(f'Partida {soma} Cuidado')
        else:
            print(f'Partida {soma} Atenção') 

def teste_funcional():
    chamda_scrapi()
    with open('partida.json', 'r+') as file:
        partida = json.load(file)
        dados_time(partida['povo'], partida['robo'])

def teste_automatizar():
    cont = 0
    while cont < 4:
        teste_funcional()
        sleep(30)
        cont = cont + 1
        


    
