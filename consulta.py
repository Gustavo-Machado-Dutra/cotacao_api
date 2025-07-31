
import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Pega a chave da API
KEY = os.environ.get('API_KEY')
# URL da API de taxas de câmbio
url = f'https://v6.exchangerate-api.com/v6/{KEY}/latest/USD'


requests = requests.get(url)

# se a requisição for bem-sucedida, imprime os dados
if requests.status_code == 200:
    data = requests.json() # Converte a resposta JSON em um dicionário

    conversoes = data.get("conversion_rates", {})

    # Lista de moedas que queremos exibir
    moedas = ["BRL", "EUR"]

    print("Cotação do Dólar (USD):")

for moeda in moedas:
    valor = conversoes.get(moeda)   # Obtém o valor da moeda específica para achar o valor da cotação
    if valor:
        print(f"1 USD = {valor:.2f} {moeda}")




