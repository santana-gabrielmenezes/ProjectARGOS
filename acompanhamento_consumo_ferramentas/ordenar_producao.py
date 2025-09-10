# %%
import pandas as pd
import glob
import os
# %%
caminho_diretorio = 'base_dados_producao'
todos_arquivos = glob.glob(os.path.join(caminho_diretorio,'producao*.csv'))
todos_arquivos
#%%
lista_dfs = []
for arquivo in todos_arquivos :
    df_temp = pd.read_csv(arquivo)
    lista_dfs.append(df_temp)

df_producao = pd.concat(lista_dfs,ignore_index=True)
df_producao
# %%
