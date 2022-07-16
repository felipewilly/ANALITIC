from time import sleep
from datetime import datetime, timedelta, time
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

def teste_funcional():
    chamda_scrapi()
    soma = soma_media()
    if soma > 67: 
        print(f'Media: {soma:.2f}, Entrada.')
    elif soma <= 56:
        print(f'Risco: {soma:.2f}, Observa.')
    else:
        print(soma)

def teste_automatizar():
    at = Cascudo()
    atualiza = at.abrir()
    saida = at.atualiz(atualiza)
    barcelona = Altomatizou(saida[0]['HC'])
    barcelona.bloco_one()
    print(barcelona.bloco_one())
    while barcelona.bloco_one() is True:
        sleep(10)
        print('Jogo rolando')


def soma_media():
    time = Cascudo()
    atualiza = time.abrir()
    saida = time.atualiz(atualiza)
    soma = (saida[0]['Ataque'] + saida[0]['Posse'] + saida[1]['povo'] + saida[1]['robo']) / 4
    return soma


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

class Altomatizou():
    def __init__(self, hora):
        self.hora = hora
        self.hora_now = datetime.now()
      
    #getter
    @property
    def hora(self):
        return self._hora
    #setter
    @hora.setter
    def hora(self, valor):
        hora = valor
        horac = str(hora).split(' ')
        horad = horac[-1]      
        horae = datetime.strptime(horad, "%H:%M:%S")
        self.horaf = horae + timedelta(hours=13)
        self._hora = self.horaf.strftime("%H:%M:%S")

    def bloco_one(self):
        self.hora_now = datetime.now()
        self.bloco_set = self.horaf + timedelta(minutes=45)
        self.bloco_sets = self.bloco_set + timedelta(minutes=15)
        self.bloco_setss = self.bloco_sets + timedelta(minutes=45)

        if self.hora_now.strftime("%H:%M:%S") < self.horaf.strftime("%H:%M:%S"):
            return False  
        elif self.horaf.strftime("%H:%M:%S") >= self.hora_now.strftime("%H:%M:%S"):
            return True
        elif self.bloco_sets.strftime("%H:%M:%S") >= self.hora_now.strftime("%H:%M:%S"): 
            return False
        elif self.hora_now.strftime("%H:%M:%S") >= self.bloco_sets.strftime("%H:%M:%S"):
             return True
        elif self.hora_now.strftime("%H:%M:%S") >= self.bloco_setss.strftime("%H:%M:%S"):
            return False