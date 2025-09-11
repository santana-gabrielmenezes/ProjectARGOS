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
colunas_a_manter = {'Material' : 'Peca',
                    'Qtd.boa confirm.' : 'Producao',
                    'Data' : 'Data',
                    'CenTrab' : 'Setor',
                    'Turno': 'Turno'}
# %%
df_producao = (df_producao.rename(columns= lambda c : c.strip())
                          .rename(columns= colunas_a_manter)
                          .assign(Setor= lambda c : c['Setor'].astype(str).str[:3],
                                  Data= lambda df: pd.to_datetime(df['Dt.entrada'] + ' ' + df['Hora'], format='%Y-%m-%d %H:%M:%S')
                                  )
                          .loc[:,colunas_a_manter.values()]
                          )
df_producao
# %%
df_producao.to_csv('producao_ordenado.csv',index=False)
# %%
