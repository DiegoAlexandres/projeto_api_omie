#%%
import pandas as pd
import requests
import os
from dotenv import load_dotenv, find_dotenv
import time

#%%
load_dotenv(find_dotenv())

#%%
APP_KEY = os.getenv("OMIE_APP_KEY")
SECRET_KEY = os.getenv("OMIE_SECRET_KEY")

#%%
url = "https://app.omie.com.br/api/v1/financas/mf/"

#%%
def buscar_movimentacoes(pagina):
    payload = {
        "call" : "ListarMovimentos",
        "app_key" : APP_KEY,
        "app_secret" : SECRET_KEY,
        "param" : [{
            "nPagina" : pagina,
            "nRegPorPagina" : 500
        }],
    }
    response = requests.post(url, json=payload, timeout=60)
    return response.json()

#%%
primeira_pagina = buscar_movimentacoes(1)
primeira_pagina

#%%
total_paginas = primeira_pagina["nTotPaginas"]
total_paginas

#%%
movimentacao = []

#%%
for pagina in range(1, total_paginas + 1):
    dados = buscar_movimentacoes(pagina)
    movimentacao.extend(dados["movimentos"])
    print(f"Página: {pagina} OK")
    time.sleep(1)
    
print("Total Coletado:", len(movimentacao))

#%%
df = pd.json_normalize(movimentacao)
df

#%%
#=========================================TRATAMENTO DE DADOS=================================================
colunas = [
    "detalhes.cCodCateg",
    "detalhes.cGrupo",
    "detalhes.cNatureza",
    "detalhes.cNumParcela",
    "detalhes.cStatus",
    "detalhes.dDtEmissao",
    "detalhes.dDtPrevisao",
    "detalhes.dDtRegistro",
    "detalhes.dDtVenc",
    "detalhes.nCodCC",
    "detalhes.nCodCliente",
    "detalhes.nValorTitulo",
    "resumo.nDesconto",
    "resumo.nJuros",
    "resumo.nMulta",
    "resumo.nValAberto",
    "resumo.nValLiquido",
    "resumo.nValPago",
]

#%%
df_tratado = df[colunas].copy()
df_tratado

#%%
df_tratado = df_tratado.rename(columns={
    "detalhes.cCodCateg"   : "id_categoria",
    "detalhes.cGrupo"      : "grupo",
    "detalhes.cNatureza"   : "natureza",
    "detalhes.cNumParcela" : "parcela",
    "detalhes.cStatus"     : "status",
    "detalhes.dDtEmissao"  : "data_emissao",
    "detalhes.dDtPrevisao" : "data_previsao",
    "detalhes.dDtRegistro" : "data_registro",
    "detalhes.dDtVenc"     : "data_vencimento",
    "detalhes.nCodCC"      : "id_conta_corrente",
    "detalhes.nCodCliente" : "id_cliente",
    "detalhes.nValorTitulo": "valor_titulo",
    "resumo.nDesconto"     : "desconto",
    "resumo.nJuros"        : "juros",
    "resumo.nMulta"        : "multa",
    "resumo.nValAberto"    : "valor_aberto",
    "resumo.nValLiquido"   : "valor_liquido",
    "resumo.nValPago"      : "valor_pago",
})
df_tratado

#%%
df_tratado.info()

#%%
colunas_valor = [
    "valor_titulo", "desconto", "juros", "multa",
    "valor_aberto", "valor_liquido", "valor_pago"
]

#%%
df_tratado[colunas_valor] = df_tratado[colunas_valor].astype("float64")

#%%
df_tratado.info()

#%%
df_tratado

#%%
colunas_data = ["data_emissao", "data_previsao", "data_registro", "data_vencimento"]

#%%
for coluna in colunas_data:
    df_tratado[coluna] = pd.to_datetime(df_tratado[coluna], format="%d/%m/%Y", errors="coerce")

#%%
df_tratado

#%%
df_tratado.info()

#%%
df_tratado = df_tratado.reset_index(drop=True)
df_tratado

#%%
df_tratado

#%%
df_tratado.info()