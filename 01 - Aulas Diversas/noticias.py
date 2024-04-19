# Alex Felipe Barbosa 18/04/2024
# 03 - Como Pegar Notícias Automaticamente com Python

# Raspagem de Dados

# Beautiful soup

import requests 
import bs4


# Noticias do SPFC
url = 'https://ge.globo.com/futebol/times/sao-paulo/'

requisicao = requests.get(url)

pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")

# Pegar os elementos "a" que tenham a classe "feed-post-link"

lista_noticias = pagina.find_all("a", class_="feed-post-link")

for noticia in lista_noticias:
  print(noticia.text)
  print(noticia.get("href"))
  print('-------------------------------------------------')

