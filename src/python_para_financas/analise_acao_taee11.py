#%%
import pandas as pd
import yfinance as yf

#%%
taesa = yf.Ticker("TAEE11.SA")
historico = taesa.history(period="5y")

#%%
historico.head()

#%%
dividendos_filtrados = historico["Dividends"]

#%%
dividendos_filtrados

#%%
dividendos_filtrados = dividendos_filtrados[dividendos_filtrados > 0]

#%%
dividendos_filtrados

#%%
dados = pd.DataFrame(dividendos_filtrados).reset_index()

#%%
dados

#%%
soma_dividendos = dados["Dividends"].sum()

#%%
soma_dividendos

#%%
media_dividendos = soma_dividendos / 5 

#%%
media_dividendos

#%%
def preco_teto(pagamento_medido, retorno_esperado):
    return pagamento_medido / retorno_esperado

#%%
preco_teto(media_dividendos, 0.06)

#%%
preco_teto(media_dividendos, 0.08)

#%%
preco_teto(media_dividendos, 0.10)