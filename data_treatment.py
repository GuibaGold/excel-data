import data_extraction as data
import pandas as pd
import numpy as np


df_carga = data.carga_to_csv()
df_base = data.base_to_csv()
df_base_filtered = df_base[["Nº ANTIGO DO BEM              (ANTES do inventArio):","DESCRICAO COMPLETA DO BEM:"]].dropna("index", how="any")


string_list_carga = list(df_carga["tombamento"].astype(str))
new_list = []
for string in string_list_carga:
    string_ = str(string).replace(".","").lstrip("0")
    new_list.append(string_)

df_base_filtered["tombamento"] = df_base_filtered["Nº ANTIGO DO BEM              (ANTES do inventArio):"]
df_carga["tombamento"] = new_list

# criando novo dataframe com labels identicas ao df_carga
novo_df_base = pd.DataFrame()
novo_df_base["tombamento"] = df_base_filtered["Nº ANTIGO DO BEM              (ANTES do inventArio):"]
novo_df_base["descricao"] = df_base_filtered["DESCRICAO COMPLETA DO BEM:"]

novo_df_base.to_csv("base_limpo.csv")

df_base_limpo = pd.read_csv("base_limpo.csv")
df_final = pd.DataFrame()
df_final = df_carga[df_carga["tombamento"].isin(df_base_limpo["tombamento"])][["tombamento", "descrição ", "aquisição", "incorporação", "valor"]]
print()
df_carga.drop(df_final.index).to_csv("final.csv")





    
   



