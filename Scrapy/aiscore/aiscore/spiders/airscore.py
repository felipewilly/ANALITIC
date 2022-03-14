import scrapy
from back.dados import retorno_url

class AirscoreSpider(scrapy.Spider):
         
        dados = retorno_url()
        name = 'airscore'
        start_urls = dados['link']
      
        def parse(self, response):
            if dados['time'] == 'a':
                dados = response.selector.xpath('//*[@id="Live"]/div[1]/div[4]/div[4]/div[4]/div[1]/div[2]/div/div/div/div').get()
            if dados['time'] == 'b':
                dados = response.selector.xpath('//*[@id="Live"]/div[1]/div[4]/div[4]/div[4]/div[3]/div[1]/div/div/div/div').get()
            time_casa = int(dados[49:51])
            yield{
                'Ataque': time_casa
            }

class Tratamento():
    def teste():
        print('teste')

 