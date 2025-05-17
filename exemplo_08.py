import requests
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
# This code fetches the current spot price of Bitcoin in USD from the Coinbase API. 

# Configurações do banco de dados
DATABASE_URL = os.getenv("DATABASE_KEY")
# Criação do engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definição do modelo de dados
class BitcoinDados(Base):
    __tablename__ = "bitcoin_dados"
    
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timestamp = Column(DateTime)

# Cria a tabela (se não existir)
Base.metadata.create_all(engine)

# This code fetches the current spot price of Bitcoin in USD from the Coinbase API. 
def extrair():
    # This function extracts the current spot price of Bitcoin in USD from the API response.
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url)
    return response.json()
    
def transformar(dados):
#Transforma os dados brutos da API e adiciona timestamp."""
        valor = float(dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        dados_transformados = BitcoinDados(
            valor = valor,
            criptomoeda = criptomoeda,
            moeda = moeda,
            timestamp = datetime.now()
        )
        return dados_transformados

def carregar(dados):
    #Salva os dados no PostgreSQL usando SQLAlchemy."""
    with Session() as session:
            session.add(dados)
            session.commit()
            print("Dados inseridos com sucesso no PostgreSQL.")
            # Verifica se os dados já existem no banco de dados 

if __name__ == "__main__":
    while True:
        # Extração e tratamento dos dados      
        dados_json = extrair()
        dados_transformados = transformar(dados_json)
        print("Dados transformados:")
            
        carregar(dados_transformados)
           
        print("Aguardando 15 segundos para a próxima requisição...")
        sleep(15)  
        # Espera 115 segundos antes de fazer a próxima requisição
        # dados_json = extrair()        
