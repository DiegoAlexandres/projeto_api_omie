#%%
import pandas as pd
import requests
import os
from dotenv import load_dotenv, find_dotenv

#%%
load_dotenv(find_dotenv())

#%%
APP_KEY = os.getenv("OMIE_APP_KEY")
SECRET_KEY = os.getenv("OMIE_SECRET_KEY")

#%%
url = "https://app.omie.com.br/api/v1/financas/mf/"
payload = {
    "call" : "ListarMovimentos",
    "app_key" : APP_KEY,
    "app_secret" : SECRET_KEY,
    "param" : [{
        "nPagina" : 1,
        "nRegPorPagina" : 500
    }],
}

#%%
response = requests.post(url, json=payload, timeout=60)
print("Status: ", response.status_code)

#%%
dados = response.json()
dados

#%%
movimentacao = dados["movimentos"]
movimentacao

#%%
df = pd.json_normalize(movimentacao)
df