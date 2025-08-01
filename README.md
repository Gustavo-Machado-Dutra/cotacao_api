# 💱 Cotação de Moedas com Exchangerate API

Este é um script Python simples que consulta a **cotação do dólar americano (USD)** em relação a outras moedas (como **BRL** e **EUR**) utilizando a [Exchangerate API](https://www.exchangerate-api.com/).

---

## 🚀 Como funciona

O script:

1. Lê uma chave de API do arquivo `.env`;
2. Consulta a cotação atual via requisição `GET`;
3. Mostra o valor atual de conversão do USD para as moedas escolhidas.

---

## 📦 Requisitos

- Python 3.10+
- Uma chave gratuita da [Exchangerate API](https://www.exchangerate-api.com/)

Instale os pacotes necessários com:

```pip install -r requirements.txt ```


## 🛠️ Configuração

- Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

API_KEY = sua_chave_aqui

Substitua sua_chave_aqui pela sua chave da API.
