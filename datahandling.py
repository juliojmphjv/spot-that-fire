import gmplot
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from geopy import Nominatim
import time
import unicodedata
import re


dataframe = pd.read_csv('datawarehouse/VIIRS_I_South_America_VNP14IMGTDL_NRT_2019291.txt')

geolocator = Nominatim(user_agent="SpotThatFire", timeout=5)

def removerAcentosECaracteresEspeciais(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def parse_country(addr):

    countries = pd.read_csv('datawarehouse/countrys.csv', delimiter=';')

    for country in countries.index:

        if str(countries.loc[country, 'Pais']) in addr.split():
            return str(countries.loc[country, 'Pais'])

def parse_state(addr):

    state_code = pd.read_csv('datawarehouse/state_codes.csv', delimiter=';')

    for code in state_code.index:

        if str(state_code.loc[code, 'SIGLA']) in addr.split():
            return str(state_code.loc[code, 'SIGLA'])

x = 0
dicionario = {'latitude': [], 'longitude': [], 'state': []}
for row in dataframe.index:
    lat = str(dataframe.loc[row, 'latitude'])
    lon = str(dataframe.loc[row, 'longitude'])
    address = geolocator.reverse(lat+' '+lon)
    cleaned = removerAcentosECaracteresEspeciais(str(address))
    pais = parse_country(cleaned)
    estado = parse_state(cleaned)
    dicionario['latitude'].append(lat)
    dicionario['longitude'].append(lon)
    dicionario['state'].append(estado+' '+pais)
    time.sleep(1)
    x+=1
    if x>=10: break

df_statistic_bystate = pd.DataFrame.from_dict(dicionario)
df_statistic_bystate.to_csv('locations')
print(df_statistic_bystate.head())



# if __name__ == '__main__':
#     cleaned = removerAcentosECaracteresEspeciais('Vila Velha, Oiapoque, Microrregião de Oiapoque, Mesorregião do Norte do Amapá, AP, Região Norte, Brasil')
#     print(parse_country(cleaned))
#     print(parse_state(cleaned))