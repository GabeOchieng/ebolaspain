import bs4
import requests
import re

data = {}

response = requests.get('http://es.wikipedia.org/wiki/%C3%89bola_en_Espa%C3%B1a')
soup = bs4.BeautifulSoup(response.text)

res = re.search('Enfermos repatriados <b>(?P<er>[0-9]+)</b>',response.text)
if res:
	data['es_repatriados'] = res.group('er')


res = re.search('Contagios confirmados <b>(?P<cc>[0-9]+)</b>',response.text)
if res:
	data['es_contagios'] = res.group('cc')

res = re.search('Personas aisladas <b>(?P<pa>[0-9]+)</b>',response.text)
if res:
	data['es_aislamiento'] = res.group('pa')

res = re.search('Personas en seguimiento <b>(?P<ps>[0-9]+)</b>',response.text)
if res:
	data['es_seguimiento'] = res.group('ps')

print data



