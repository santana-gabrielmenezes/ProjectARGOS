# %%
import pandas as pd
import glob
import os
# %%
caminho_diretorio = 'base_dados_producao'
todos_arquivos = glob.glob(os.path.join(caminho_diretorio,'producao*.csv'))
todos_arquivos
# %%
df_producao = pd.concat([pd.read_csv(f,decimal='.') for f in todos_arquivos]
                        ,ignore_index=True
                        )
df_producao
# %%
colunas_a_manter = {'Material' : 'Peca',
                    'Qtd.boa confirm.' : 'Producao',
                    'Dt.entrada' : 'Data',
                    'Hora' : 'Hora',
                    'CenTrab' : 'Setor'}
# %%
df_producao = (df_producao.rename(columns= lambda c : c.strip())
                          .rename(columns= colunas_a_manter)
                          .assign(Setor= lambda c : c['Setor'].astype(str).str[:3])
                          .loc[:,colunas_a_manter.values()]
                          )
df_producao
# %%
df_producao.to_csv('producao_ordenado.csv', index=False, decimal=',')
# %%
