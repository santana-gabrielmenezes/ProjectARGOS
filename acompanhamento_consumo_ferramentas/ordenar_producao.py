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
                    'Dt.entrada' : 'Data',
                    'Hora' : 'Hora',
                    'CenTrab' : 'Setor',
                    'Turno': 'Turno'}
# %%
df_producao = (df_producao.rename(columns= lambda c : c.strip())
                          .rename(columns= colunas_a_manter)
                          .assign(Setor= lambda c : c['Setor'].astype(str).str[:3])
                          .loc[:,colunas_a_manter.values()]
                          )
df_producao
# %%
df_producao['Peca'].str[-2].str.isalpha()
# %%
condicao_F = df_producao['Peca'].str[-3] == 'F'
df_producao.loc[condicao_F, 'Peca'] = df_producao['Peca'].str[:-3]

condicao_letra = df_producao['Peca'].str[-2].str.isalpha()
df_producao.loc[condicao_letra, 'Peca'] = df_producao['Peca'].str[:-2]
df_producao
# %%
