import pandas as pd
import csv
import xlrd

def read_excel_to_csv():
    wb = xlrd.open_workbook("xlsx_files/base_final.xlsx")
    sh_content = wb.sheet_by_name("BASE GERAL")
    write_csv(sh_content)


def write_csv(sh_content):
    your_csv_file = open("base_final.csv", 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for row_index in range(sh_content.nrows):
        row = sh_content.row_values(row_index)
        wr.writerow(row)

    your_csv_file.close()