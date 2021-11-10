from datetime import datetime
from xlrd import xldate_as_tuple
import xlrd,xlwt
from xlutils.copy import copy



# 获取登录测试用例
def get_body(excelName,sheetName):
    #打开工作簿
    workbook = xlrd.open_workbook(excelName)
    #指定sheet名读取
    stand_sheet = workbook.sheet_by_name(sheetName)
    #按行存储测试用例
    value_rows = []
    #获取sheet中有多少条用例
    nrows = stand_sheet.nrows
    cols = stand_sheet.ncols
    """
    excel表中的数用xlrd读取会出现int型变float型,所以需要转换
    python读取excel中单元格的内容返回的有5种类型，即ctype:
    ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    """
    for i in range(1,nrows):    #遍历所有行
        row_content = []
        for j in range(cols):   #遍历所有列
            ctype = stand_sheet.cell(i, j).ctype   # 表格的数据类型
            cell = stand_sheet.cell_value(i, j)    #表格的数据
            if ctype == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
            elif ctype == 3:
                # 转成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m %H:%M:%S')
            elif ctype == 4:
                cell = True if cell == 1 else False
            row_content.append(cell)    #每一列都加入列表
        row_content.pop()   #去除最后一列:是否通过列
        row_content.append(i)   #加入每列行号,方便将测试结果写入excel
        value_rows.append(row_content)  #将列加入到value_rows中

    return value_rows


#写入测试结果
def wt_result(excelName,sheetName,i,j,value,sheetCount):
    # 打开工作簿
    workbook = xlrd.open_workbook(excelName)
    #复制工作簿
    excel = copy(wb = workbook)
    #指定sheet,只能用索引序号指定
    excel_table = excel.get_sheet(sheetCount)
    stand_sheet = workbook.sheet_by_name(sheetName)
    #写入指定行,列,值
    excel_table.write(i,j,value)
    #保存,如果相同名称即为写入
    excel.save(excelName)

# get_body('bank.xls', 'Login_Test_Case')
# wt_result('bank.xls', 'Deposit_Test_Case',1,4,'通过',1)
# if __name__ == '__main__':
#     ex = Excel()
#     ex.get_body('bank.xls', 'Login_Test_Case')