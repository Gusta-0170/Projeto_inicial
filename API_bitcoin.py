import requests
import json
# This code fetches the current spot price of Bitcoin in USD from the Coinbase API. 
url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

response = requests.get(url)

print(response.json())

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
            'moeda': moeda
        }
        return dados_transformados
    
    if __name__ == "__main__":
        dados_json = extrair()
        dados_transformados = transformar(dados_json)
        print(dados_transformados)
