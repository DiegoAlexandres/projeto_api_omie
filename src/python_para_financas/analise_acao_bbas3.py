#%%
import pandas as pd
import yfinance as yf

#%%
bbas3 = yf.Ticker("BBAS3.SA")
historio = bbas3.history(period="5y")

#%%
historio

#%%
dados = historio[historio["Dividends"] > 0].reset_index()

#%%
dados

#%%
soma_dividendos = dados["Dividends"].sum()
soma_dividendos

#%%
pagamento_medio = soma_dividendos / 5
pagamento_medio

#%%
def preco_teto(pagamento_medido, retorno_esperado):
    resultado = pagamento_medido / retorno_esperado
    return resultado

#%%
preco_teto(pagamento_medio, 0.06)

#%%
dados.tail()

#%%
preco_teto(pagamento_medio, 0.08)

#%%
preco_teto(pagamento_medio, 0.10)
    