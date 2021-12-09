
#coded by U4I5

# Importation des Modules

from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests
import os

# Url du site Wallhaven catégorie Random
url = 'https://wallhaven.cc/random' 
#Récupération response de la page 

r = requests.get(url).content
soup = BeautifulSoup(r, "lxml")
wall_tag = soup.findAll('a', href=True)
#wall = "https://wallhaven.cc/w/"


for links in wall_tag:
    print(links.get('href'))




#'https://wallhaven.cc/w/


