
import scrapy
import json


class AirscoreSpider(scrapy.Spider):
    dd = {}
    with open('..////partida.json', 'r+') as file:
        dd = json.load(file)
    global dados
    dados = dd #vai abrir o arquivo pincipal chamado dd e vai buscar o link e o time 
    name = 'aiscore'
    start_urls = [dados['link']]
    
    def parse(self, response):
        horario_camp = response.selector.css('.mediaTitle::text').get()
        hora_convert = str(horario_camp).strip()
        if dados['campo'] == 'a':
            try:
                time_casa = response.selector.xpath('//*[@id="Live"]/div[1]/div[4]/div[4]/div[4]/div[1]/div[2]/div').get()
                time_casa = int(time_casa[39:41])
                time_casa_posse = response.selector.xpath('//*[@id="Stats"]/div[3]/div[1]/div[1]/span[1]').get()
                time_casa_posse = int(time_casa_posse[22:24])
                time_casa_nome = response.selector.css('.home-box .font-500 a::text').get()
                time_casa_nomec = str(time_casa_nomec).strip()

                yield{'Ataque': time_casa, 'Posse': time_casa_posse, 'Time': 'Casa', 'Nome': time_casa_nome, 'HC': hora_convert}

            except:
                print('BLOCO 2 EXECUTADO') #aguardando biblioteca de loogin
                time_casa = response.selector.xpath('//*[@id="Live"]/div[1]/div[3]/div[4]/div[4]/div[1]/div[2]/div').get()
                time_casa = int(time_casa[39:41])
                time_casa_posse = response.selector.xpath('//*[@id="Stats"]/div[3]/div[1]/div[1]/span[1]').get()
                time_casa_posse = int(time_casa_posse[22:24])
                time_casa_nome = response.selector.css('.home-box .font-500 a::text').get()
                time_casa_nomec = str(time_casa_nome).strip()

                yield{'Ataque': time_casa, 'Posse': time_casa_posse, 'Time': 'Casa', 'Nome': time_casa_nome, 'HC': hora_convert}
            else:
               print('CODICO EXECUTADO')

        if dados['campo'] == 'b':
            try:
                time_visita = response.selector.xpath('//*[@id="Live"]/div[1]/div[4]/div[4]/div[4]/div[3]/div[1]/div').get()
                time_visita = int(time_visita[39:41])
                time_visita_nome = response.selector.css('.away-box .font-500 a::text').get()
                time_visita_posse = response.selector.xpath('//*[@id="Stats"]/div[3]/div[1]/div[1]/span[3]').get()
                time_visita_posse = int(time_visita_posse[22:24])
                yield{'Ataque': time_visita, 'Posse': time_visita_posse, 'Time': 'Visitante', 'Nome': time_visita_nome, 'HC': hora_convert}

            except:
                print('BLOCO 2 EXECUTADO')
                time_visita = response.selector.xpath('//*[@id="Live"]/div[1]/div[3]/div[4]/div[4]/div[3]/div[1]/div').get()
                time_visita = int(time_visita[39:41])
                time_visita_nome = response.selector.css('.away-box .font-500 a::text').get()

                time_visita_posse = response.selector.xpath('//*[@id="Stats"]/div[3]/div[1]/div[1]/span[3]').get()
                time_visita_posse = int(time_visita_posse[22:24])
                yield{'Ataque': time_visita, 'Posse': time_visita_posse, 'Time': 'Visitante', 'Nome': time_visita_nome, 'HC': hora_convert}

            else:
                print('CODICO EXECUTADO')
    


