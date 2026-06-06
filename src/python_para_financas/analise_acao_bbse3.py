#%%
import pandas as pd
import yfinance as yf

#%%
bbse3 = yf.Ticker("BBSE3.SA")
historico = bbse3.history(period="5y")

#%%
historico

#%%
dividendos_filtrado = historico["Dividends"]

#%%
dividendos_filtrado

#%%
dividendos_filtrado = dividendos_filtrado[dividendos_filtrado > 0]

#%%
dividendos_filtrado

#%%
dados = pd.DataFrame(dividendos_filtrado).reset_index()

#%%
dados

#%%
soma_dividendos = dados["Dividends"].sum()

#%%
soma_dividendos

#%%
pagamento_medio = soma_dividendos / 5
pagamento_medio

#%%
def preco_teto(pagamento_medio, retorno_esperado):
    return pagamento_medio / retorno_esperado

#%%
preco_teto(pagamento_medio, 0.06)

#%%
preco_teto(pagamento_medio, 0.08)

#%%
preco_teto(pagamento_medio, 0.10)