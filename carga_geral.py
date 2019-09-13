import pandas as pd
import xlrd


def read_excel_to_csv():
    df = pd.ExcelFile("xlsx_files/carga_geral.xlsx").parse("Plan1")
    return df

read_excel_to_csv()



