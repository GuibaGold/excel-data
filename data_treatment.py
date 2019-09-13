import carga_geral
import base_final
import pandas as pd


df_carga = carga_geral.read_excel_to_csv()
df_base = base_final.read_excel_to_csv()

print(df_base["Nº ANTIGO DO BEM              (ANTES do inventArio):"])

final_list =["Tombamento"]
final_list_descricao = ["Descricao"]
for item_carga in list(df_carga["tombamento"]):
    if not item_carga in list(df_base["Nº ANTIGO DO BEM              (ANTES do inventArio):"]):
        final_list.append(item_carga)

print(len(list(df_carga["tombamento"])), len(list(df_base["Nº ANTIGO DO BEM              (ANTES do inventArio):"])), len(final_list))
df_final = pd.DataFrame(final_list)
df_base.to_csv("base.csv")
df_carga.to_csv("carga.csv")
df_final.to_csv("final.csv")
    
   



