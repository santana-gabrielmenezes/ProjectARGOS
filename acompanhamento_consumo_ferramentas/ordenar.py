# %%
import pandas as pd
# %%
df_ferramentas = pd.read_csv('consumo_ferramentas.csv')
df_ferramentas
# %%
df_ferramentas.columns = df_ferramentas.columns.str.strip()
df_ferramentas
# %%
df_ferramentas_dropcolumns = df_ferramentas.drop(columns=['Lote',
                                                          'Motivo do movimento',
                                                          'Tipo de movimento',
                                                          'Nome do usuário',
                                                          'Data de entrada',
                                                          'Centro',
                                                          'Depósito',
                                                          'Item doc.material',
                                                          'Doc.material',
                                                          'Ordem',
                                                          'Fornecedor',
                                                          'Pedido',
                                                          'Estoque especial',
                                                          'Item',
                                                          'Contador',
                                                          'Ordem do cliente',
                                                          'Texto cab.documento',
                                                          'Unid.prç.pedido',
                                                          'Referência',
                                                          'Unnamed: 26'
                                                          ])
df_ferramentas_dropcolumns
# %%
df_ferramentas_renamecolumns = df_ferramentas_dropcolumns.rename(columns= {'Texto breve material' : 'Descrição',
                                                                          'Data de lançamento' : 'Data',
                                                                          'Qtd.  UM registro' : 'Quantidade',
                                                                          'Montante em MI' : 'Valor',
                                                                          'Hora do registro' : 'Hora',
                                                                          'Centro custo' : 'Setor'
                                                                           })
df_ferramentas_renamecolumns
# %%
df_ferramentas_setor = df_ferramentas_renamecolumns
df_ferramentas_setor['Setor'] = (df_ferramentas_setor['Setor'].astype(str)
                                                              .str[-3:])
df_ferramentas_setor
# %%
df_ferramentas_sinais = df_ferramentas_setor
df_ferramentas_sinais['Quantidade'] = df_ferramentas_sinais['Quantidade'] * -1
df_ferramentas_sinais['Valor'] = df_ferramentas_sinais['Valor'] * -1
df_ferramentas_sinais
# %%
df_ferramentas_final = (df_ferramentas_sinais.sort_values(by=['Data','Hora'], ascending=True)
                                             .reset_index(drop=True)
                                             )
# %%
