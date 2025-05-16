import requests
import json
from tinydb import TinyDB
from datetime import datetime
import time
# This code fetches the current spot price of Bitcoin in USD from the Coinbase API. 

db = TinyDB('db.json')
# This code fetches the current spot price of Bitcoin in USD from the Coinbase API. 
def extrair():
    # This function extracts the current spot price of Bitcoin in USD from the API response.
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url)
    return response.json()
    
def transformar(dados):
        valor = (dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        dados_transformados = {
            'valor': valor,
            'criptomoeda': criptomoeda,
            'moeda': moeda,
            'timestamp': datetime.now().isoformat()
                    }
        return dados_transformados

def carregar(dados_transformados):
       db = TinyDB('db.json')
       db.insert(dados_transformados)
       print("Dados inseridos com sucesso no banco de dados.")

if __name__ == "__main__":
        while True:
        ############### EXTRACAO ###############        
            dados_json = extrair()
            dados_transformados = transformar(dados_json)
            carregar(dados_transformados)
            time.sleep(5)  # Espera 1 minuto antes de fazer a próxima requisição
        # dados_json = extrair()        
