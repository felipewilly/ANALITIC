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
    deve rodar dentro do modulo com scrapy.cfg
    '''
    os.system('scrapy crawl aiscore -O airscore.json --nolog')
    
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
    with open('../partida.json', 'w') as file:
        partida['povo'] = int(input('Dados do Povo: '))
        partida['robo'] = int(input('Dados do Robo: '))
        partida['link'] = str(input('Url:'))
        partida['campo'] = str(input('Casa[A] ou Visitante[B]: '))
        json.dump(partida, file)
    return chamda_scrapi()

def chama_dicionarios():
    time = Cascudo()
    atualiza = time.abrir()
    saida = time.atualiz(atualiza)
    for i in saida[:]:
        for k, v in i.items():
            print(f'{k}: {v}')

def dados_time():

    with open('airscore.json', 'w+') as file:
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

class Cascudo:
    def __init__(self) -> None:
        self.vasco = list()
        self.arquivo = dict()
    
    def abrir(self):
        with open('././airscore.json','rb') as file:
            self.arquivo = json.load(file)
            return self.arquivo
                
    def atualiz(self, fora):       
        self.vasco = fora[:]
        with open('../partida.json', 'rb') as file:
            arquivo_at = json.load(file)
            self.vasco.append(arquivo_at)
            return self.vasco