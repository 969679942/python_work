import xlrd
import pypinyin

#销售占比计算
def proportion_count(name,all_sales_count):
    proportion = format(round(name / all_sales_count,4),'.2%')
    return proportion


#种类汉字转拼音
def name_pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word,style=pypinyin.NORMAL):
        s +=''.join(i)
    return s

#种类去重
def kind_removal():
    rdexcel = xlrd.open_workbook("12月份衣服销售数据.xlsx")
    sheet = rdexcel.sheet_by_name("12月份各种服饰销售情况")
    list1,list2 = [],[]
    for i in range(1,sheet.nrows):
        list1.append(sheet.cell_value(i,1))
    list1 = sorted(set(list1),key=list1.index)
    for j in list1:
        list2.append(name_pinyin(j))
    kind_dict = dict(zip(list2,list1))
    return kind_dict

#计算销售额占比
def proportion_sales(sales_money = 0):
    rdexcel = xlrd.open_workbook("12月份衣服销售数据.xlsx")
    sheet = rdexcel.sheet_by_name("12月份各种服饰销售情况")
    all_sales_money = 0
    money_dict = {}
    for key,value in kind_removal().items():
        for i in range(sheet.nrows):
            if value == sheet.cell_value(i,1):
                sales_money += sheet.cell_value(i,2)*sheet.cell_value(i,4)
        money_dict[key] = sales_money
        all_sales_money += sales_money
        sales_money = 0
    globals().update(money_dict)
    for key,value in money_dict.items():
        globals()[key] = proportion_count(globals()[key],all_sales_money)
        print(f'{kind_removal()[key]}的销售额占比为：{globals()[key]}')
    print(f'总销售额为：{all_sales_money}')

#计算所有种类的月销售占比
def proportion(count = 0):
    rdexcel = xlrd.open_workbook("12月份衣服销售数据.xlsx")
    sheet = rdexcel.sheet_by_name("12月份各种服饰销售情况")
    all_sales_count = 0
    count_dict = {}
    for key,value in kind_removal().items():
        for i in range(sheet.nrows):
            if value == sheet.cell_value(i,1):
                count += sheet.cell_value(i,4)
        count_dict[key] = count
        print()
        all_sales_count += count
        count = 0
    globals().update(count_dict)
    for key,value in count_dict.items():
        print(f'{kind_removal()[key]}的平均每日销售数量为：{int(int(globals()[key]) / 30)}')
        globals()[key] = proportion_count(globals()[key],all_sales_count)
        print(f'{kind_removal()[key]}的月销售占比为{globals()[key]}')

proportion_sales()
print()
proportion()