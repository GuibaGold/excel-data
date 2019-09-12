import csv
import pandas as pd
import xlrd


def read_csv():
    df_list = []
    for csv_index in range(2, 78):
        data_frame = pd.read_csv("csv_files/carga_geral_Sheet" + str(csv_index) + ".csv")
        df_list.append(data_frame)

    new_df = pd.concat(df_list)
    new_df.to_csv("./carga_geral.csv")
    print(new_df)

    


def read_excel_to_csv():
    wb = xlrd.open_workbook("xlsx_files/carga_geral.xlsx")
    cell_list = []
    
    for sheet_index in range(1, wb.nsheets):
        sh_content = wb.sheet_by_name("Sheet" + str(sheet_index+1))
        write_csv(sh_content)


def write_csv(sh_content):
    your_csv_file = open("csv_files/carga_geral_" + sh_content.name + ".csv", 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for row_index in range(8, sh_content.nrows):
        cell = sh_content.cell(row_index, 0)
        row = sh_content.row_values(row_index)
        if cell.ctype == 1 and cell.ctype != 0:
            wr.writerow(row)
   

    your_csv_file.close()