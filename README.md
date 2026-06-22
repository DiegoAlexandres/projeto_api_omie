# Projeto API Omie

Extração de dados financeiros e cadastrais via API REST do Omie ERP, com tratamento e normalização em Python. Projeto desenvolvido para o canal **OpenBI** no YouTube.

## Sobre o projeto

A API do Omie retorna dados em JSON aninhado, comum em integrações de ERP. Este projeto cobre o fluxo completo de extração: autenticação via variáveis de ambiente, requisição POST aos endpoints, e normalização do JSON em DataFrame tabular pronto para análise.

## Endpoints integrados

**Categorias** (`/geral/categorias/`)
- Chamada `ListarCategorias` com paginação
- Normalização do retorno em DataFrame

**Movimentações financeiras** (`/financas/mf/`)
- Chamada `ListarMovimentos` com paginação
- Normalização do retorno em DataFrame

## Tecnologias

![Python](https://img.shields.io/badge/Python-FFD43B?style=flat-square&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-000000?style=flat-square&logo=python&logoColor=white)

## Técnicas aplicadas

- Autenticação segura com variáveis de ambiente (`python-dotenv`, `find_dotenv`)
- Requisições HTTP POST com `requests`
- Normalização de JSON aninhado (`pandas.json_normalize`)
- Tratamento de paginação de API

## Como executar

1. Renomeie `.example.env` para `.env` e adicione suas credenciais:

```
OMIE_APP_KEY=sua_app_key
OMIE_SECRET_KEY=sua_secret_key
```

2. Instale as dependências e execute:

```bash
uv sync
uv run main.py
```

---

📺 Projeto produzido para o canal [OpenBI](https://www.youtube.com/@openbi) no YouTube
📫 [openbiinteligencia.com.br](https://openbiinteligencia.com.br/)
