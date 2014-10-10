from bs4 import BeautifulSoup 
import urllib2

url = "http://es.wikipedia.org/wiki/%C3%89bola_en_Espa%C3%B1a"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

data = soup.find_all("th",text="Afectados")

print data.next_sibling

#print soup.prettify()



