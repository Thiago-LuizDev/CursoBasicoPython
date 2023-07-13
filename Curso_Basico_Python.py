#!/usr/bin/env python
# coding: utf-8

# **Passo a Passo de solução do Desafio**
# 
# 

# In[17]:


# Lógica de programação 

# Passo 1 - Percorrer todos os arquivos da pasta base de dados (Pasta Vendas)
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("C:/Users/Thiago Luiz/Pasta Vendas")
display(lista_arquivo)


# In[18]:


tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    # se tem "Vendas" no nome do arquivo, então
    if "Vendas" in arquivo:
        # importar o arquivo
        tabela = pd.read_csv(f"C:/Users/Thiago Luiz/Pasta Vendas/{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela])
        
# Passo 3 - Tratar / Compilar as bases de dados
display(tabela_total)


# In[19]:


# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by="Quantidade Vendida", ascending=False)
display(tabela_produtos)


# In[20]:


# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)


# In[21]:


# Passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento)
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False)
display(tabela_lojas)


# In[44]:


# Passo 7 - Criar um gráfico/dashboard
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.update_traces(marker_color='black')
grafico.show()


# In[ ]:




