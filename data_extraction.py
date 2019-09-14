import pandas as pd
from os import path

def base_to_csv():
    if path.exists("base.csv"):
        return pd.read_csv("base.csv")
    else:
        df_base = pd.ExcelFile("xlsx_files/base_final.xlsx").parse("BASE GERAL")
        df_base.to_csv("base.csv")
        return df_base

def carga_to_csv():
    if path.exists("carga.csv"):
        return pd.read_csv("carga.csv")
    else:
        df_carga = pd.ExcelFile("xlsx_files/carga_geral.xlsx").parse("Plan1")
        df_carga.to_csv("carga.csv")
        return df_carga