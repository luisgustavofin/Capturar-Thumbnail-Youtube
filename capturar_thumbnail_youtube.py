import urllib
import urllib.request
from bs4 import BeautifulSoup
import random
#IMPORT'S ^^^^^^

########################################################################
## PODE SER QUALQUER URL, FIZ SÓ MAIS ESPECÍFICO PARA AS THUMBNAILS   ##
########################################################################


print('Digite a URL do canal, já clicado na opção "VÍDEOS"')
print('EX.: "https://www.youtube.com/user/NOME DO CANAL/videos"')
digite_a_url = input('\nDigite a URL:\n')

limite_de_downloads = input('\nDigite o limite de downloads:\n')
limite_de_downloads = int(limite_de_downloads)


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = make_soup(digite_a_url)
lista_imagens = []


#COM O "." NO FINAL, A IMAGEM FICA MAIOR, SEM PERDER QUALIDADE;  "AS THUMB FICA NESSA URL LOUCA MESMA"
for img in soup.find_all('img'):
    if "i.ytimg.com" in img.get('src'):
        lista_imagens.append(img.get('src') + ".")


def download_image(url):
    name = random.randrange(1,1000) #NOMES DOS ALIATÓRIOS PARA OS ARQUIVOS
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, "C:/Users/PC/Desktop/" + full_name) #LOCAL PARA DEIXAR SALVA AS IMAGENS
        
y = 0           
for x in lista_imagens:
    y += 1
    download_image(x)
    if limite_de_downloads == y:
        break