import json



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
            
       

time = Cascudo()
atualiza = time.abrir()
saida = time.atualiz(atualiza)
for i in saida[:]:
    for k, v in i.items():
        print(k, v)

