#%%
import pandas as pd
import requests
from dotenv import load_dotenv, find_dotenv
import os

#%%
load_dotenv(find_dotenv())

#%%
APP_KEY = os.getenv("OMIE_APP_KEY")
SECRET_KEY = os.getenv("OMIE_SECRET_KEY")

#%%
url = "https://app.omie.com.br/api/v1/geral/categorias/"
payload = {
    "call" : "ListarCategorias",
    "app_key" : APP_KEY,
    "app_secret" : SECRET_KEY,
    "param" : [{
        "pagina" : 1,
        "registros_por_pagina" : 50
    }],
}

#%%
response = requests.post(url, json=payload, timeout=60)
print("Staus: ", response.status_code)

#%%
dados = response.json()
dados

#%%
categoria = dados["categoria_cadastro"]
categoria

#%%
df = pd.json_normalize(categoria)
df

#%%
#=========================================TRATAMENTO DE DADOS=================================================

df["conta_inativa"].value_counts()

#%%
df_tratado = df[df["conta_inativa"] == "N"].copy()
df_tratado

#%%
df_tratado["conta_inativa"].value_counts()

#%%
df_tratado = df_tratado[df_tratado["totalizadora"] == "N"]
df_tratado

#%%
df_tratado = df_tratado[[
    "codigo",
    "descricao",
    "dadosDRE.codigoDRE",
    "dadosDRE.descricaoDRE",
]].copy()

#%%
df_tratado

#%%
df_tratado = df_tratado.rename(columns={
    "codigo"                : "id_categoria",
    "descricao"             : "descricao_categoria",
    "dadosDRE.codigoDRE"    : "id_dre",
    "dadosDRE.descricaoDRE" : "descricao_dre",
})

#%%
df_tratado

#%%
df_tratado[["id_dre", "descricao_dre"]] = df_tratado[["id_dre", "descricao_dre"]].fillna("")
df_tratado

#%%
df_tratado = df_tratado.reset_index(drop=True)
df_tratado