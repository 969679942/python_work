import xlrd
from xlutils.copy import copy

def get_data(excelName,sheetName):
    data = []
    wb = xlrd.open_workbook(excelName)
    sheet = wb.sheet_by_name(sheetName)
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1,rows):
        row_content = []
        for j in range(0,3):
            ctype = sheet.cell(i,j).ctype
            cell = sheet.cell_value(i,j)
            if ctype == 2 and cell % 1 == 0:
                cell = int(cell)
            row_content.append(cell)
        row_content.append(i)
        row_content.append(j+1)
        data.append(row_content)
    return data

get_data('HKR.xls','LOGIN')

def wr_result(excelName,i,j,value,sheetCount):
    wb = xlrd.open_workbook(excelName)
    excel = copy(wb = wb)
    excel_sheet = excel.get_sheet(sheetCount)
    stand_sheet = wb.sheet_by_name('LOGIN')
    excel_sheet.write(i,j,value)
    excel.save(excelName)
