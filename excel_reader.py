import csv
import xlrd


def read_excel():
    wb = xlrd.open_workbook("carga_geral.xlsx")
    sh = []
    for sh_index in range(wb.nsheets):
        if sh_index != 0 and sh_index != 1:
            sh_content = wb.sheet_by_name("Sheet" + str(sh_index))
            sh.append(sh_content)
            print(sh_content.name)


read_excel()
