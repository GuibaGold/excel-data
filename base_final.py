import pandas as pd
import csv
import xlrd

def read_excel_to_csv():
    df = pd.ExcelFile("xlsx_files/base_final.xlsx").parse("BASE GERAL").dropna()
    return df.dropna("index", "all")


