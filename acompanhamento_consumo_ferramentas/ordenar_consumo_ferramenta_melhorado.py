# %%
import pandas as pd
# %% Define as colunas a serem mantidas e as renomea
colunas_a_manter = {'Material' : 'Codigo',
                    'Texto breve material' : 'Descrição',
                    'Data de lançamento' : 'Data',
                    'Hora do registro' : 'Hora',
                    'Qtd.  UM registro' : 'Quantidade',
                    'Montante em MI' : 'Valor',
                    'Centro custo' : 'Setor'
                    }
# %%
df_ferramentas = (pd.read_csv('base_dados_ferramenta/consumo_ferramentas.csv')
                    .rename(columns= lambda column : column.strip())
                    .rename(columns= colunas_a_manter)
                    .assign(Setor= lambda c : c['Setor'].astype(str).str[-3:],
                            Quantidade= lambda c : c['Quantidade'] * -1,
                            Valor= lambda c : c['Valor'] * -1
                            )
                    .sort_values(by=['Data','Hora'], ascending= True)
                    .reset_index(drop= True)
                    .loc[:,colunas_a_manter.values()]
                    )
df_ferramentas['Valor'] = df_ferramentas['Valor'].astype(str).str.replace('.',',')
df_ferramentas['Quantidade'] =df_ferramentas['Quantidade'].astype(int)
df_ferramentas
# %%
df_ferramentas.to_csv('consumo_ferramenta_ordenado.csv',index=False)
# %%
