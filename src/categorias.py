#%%
import pandas as pd
import requests
from dotenv import load_dotenv, find_dotenv
import os
import time

#%%
load_dotenv(find_dotenv())

#%%
APP_KEY = os.getenv("OMIE_APP_KEY")
SECRET_KEY = os.getenv("OMIE_SECRET_KEY")

#%%
url = "https://app.omie.com.br/api/v1/geral/categorias/"

#%%
def buscar_categorias(pagina):
    payload = {
        "call" : "ListarCategorias",
        "app_key" : APP_KEY,
        "app_secret" : SECRET_KEY,
        "param" : [{
            "pagina" : pagina,
            "registros_por_pagina" : 50
        }],
    }
    response = requests.post(url, json=payload, timeout=60)
    return response.json()

#%%
primeira_pagina = buscar_categorias(1)
primeira_pagina

#%%
total_paginas = primeira_pagina["total_de_paginas"]
total_paginas

#%%
categorias = []

#%%
for pagina in range(1, total_paginas + 1):
    dados = buscar_categorias(pagina)
    categorias.extend(dados["categoria_cadastro"])
    print(f"Páginas: {pagina} OK")
    time.sleep(1)

print("Total Coletado:", len(categorias))

#%%
df = pd.json_normalize(categorias)
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