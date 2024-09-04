import pandas as pd
import requests
from pandas import json_normalize
import random as rd
import re
from unidecode import unidecode

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://clientes.api.greenborn.com.ar/public-random-word'
# datos = requests.get(url)
# #print(datos.text)
# palabra = datos.text
# partes = re.findall(r'"(.*?)"', palabra)
# palabra = partes[0]

def obtener_palabra_dificil():
    url = 'https://clientes.api.greenborn.com.ar/public-random-word'
    datos = requests.get(url)
    palabra = datos.text
    partes = re.findall(r'"(.*?)"', palabra)
    if partes:  # Asegúrate de que partes no esté vacío
        palabra_sin_tilde= unidecode(partes[0])
        return palabra_sin_tilde # Devuelve la primera palabra obtenida de la API
    else:
        raise ValueError("No se pudo obtener una palabra de la API.")

