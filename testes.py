import json
from datetime import datetime, timedelta, time


class Cascudo:
    def __init__(self) -> None:
        self.vasco = list()
        self.arquivo = dict()
    
    def abrir(self):
        with open('Scrapy/arquivoJ/airscore.json','rb') as file:
            self.arquivo = json.load(file)
            return self.arquivo
                
    def atualiz(self, fora):       
        self.vasco = fora[:]
        with open('Scrapy/arquivoJ/partida.json', 'rb') as file:
            arquivo_at = json.load(file)
            self.vasco.append(arquivo_at)
            return self.vasco
            
t = Cascudo()
atualiza = t.abrir()
saida = t.atualiz(atualiza)
soma = (saida[0]['Ataque'] + saida[0]['Posse'] + saida[1]['povo'] + saida[1]['robo']) / 4
print(f'{soma:.2f}')

class Altomatizou():
    def __init__(self, hora):
        self.hora = hora
        self.hora_now = datetime.now().time()
    
  
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
        horae = datetime.strptime(horad, "%H:%M:%S").time()
        horae = timedelta(hours=13)
        self.horaf = horae
        self._hora = self.horaf

    def bloco_one(self):
        self.hora_now = datetime.now().time()
        self.bloco_set = self.horaf + timedelta(minutes=45)
        self.bloco_sets = self.bloco_set + timedelta(minutes=15)
        self.bloco_setss = self.bloco_sets + timedelta(minutes=45)
        print(f'HORA JOGO {self.horaf}')
        print(f'HORA 1T:  {self.bloco_set}')
        print(f'HORA 2T:  {self.bloco_sets}')
        print(f'HOR CABO: {self.bloco_setss}')
        print(self.hora_now)


        if self.hora_now > self.horaf: 
            print('Inicio do jogo: VERDADEIRO')
        elif self.bloco_set >= self.hora_now:
            print('Intervalo do jogo: FALSO')
        else:
            print('JOGO FORA DE HORA')







''''
    def bloco_one(self):
        self.hora_now = datetime.now()
        self.bloco_set = self.horaf + timedelta(minutes=45)
        self.bloco_sets = self.bloco_set + timedelta(minutes=15)
        self.bloco_setss = self.bloco_sets + timedelta(minutes=45)
        print(self.horaf)
        print(self.hora_now)
        print(self.bloco_set)
        print(self.bloco_sets)
        print(self.bloco_setss)



'''
barcelona = Altomatizou(saida[0]['HC'])
print(barcelona.bloco_one())