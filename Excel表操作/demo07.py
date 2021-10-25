import pypinyin
import xlrd

'''
全年的销售总额
每件衣服的销售额占比
每件衣服的销售（件数）占比

每件衣服的月销售占比

最畅销的衣服是那种
    每个季度最畅销的衣服
全年销量最低的衣服

'''

wb = xlrd.open_workbook(filename='2020年每个月的销售情况.xlsx',encoding_override=True)
all_sheet = wb.sheets()

quarterly_dict = {'第一季度': ['2月', '3月', '4月'], '第二季度': ['5月', '6月', '7月'], '第三季度': ['8月', '9月', '10月'],
                      '第四季度': ['11月', '12月', '1月']}
#销售占比计算
def proportion_count(name,all_sale_count,params = None):
    proportion = format(round(name / all_sale_count, 4), '.2%')
    return proportion

#汉字转拼音
def name_pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word,style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

#将所有的种类遍历到列表（数组）中进行除重，再利用pypinyin将种类名称转化为pinyin作为key，种类名称作为value存放到字典中
def kind_dict(kind_dicts = {}):
    for sheet in all_sheet:
        list_1,list_2 = [],[]
        for i in range(1,sheet.nrows):
            list_1.append(sheet.cell_value(i,1))
        list_1 = sorted(set(list_1),key=list_1.index) #列表元素去重
        for j in list_1:
            list_2.append(name_pinyin(j))
        kind_dict = dict(zip(list_2,list_1))
        kind_dicts.update(kind_dict)
    return kind_dicts

#每月销售种类字典
def mt_kind_dict(sheet):
    list_1,list_2 = [],[]
    for i in range(1,sheet.nrows):
        list_1.append(sheet.cell_value(i,1))
    list_1 = sorted(set(list_1),key=list_1.index)
    for j in list_1:
        list_2.append(name_pinyin(j))
    kd_dict = dict(zip(list_2,list_1))
    return kd_dict

#每件衣服的销售额占比,全年的销售总额
def total_annual_sales(sales_money = 0):
    all_sales_money = 0                 #全年销售总额
    money_dict = {}                     #衣服种类销售额字典
    count = 0                           #销售量
    all_count = 0                       #总销售量
    count_dict = {}                     #衣服种类销售量字典
    for key,value in kind_dict().items():
        for sheet in all_sheet:
            for i in range(sheet.nrows):
                if value == sheet.cell_value(i,1):
                    # print('类型:',type(sheet.cell_value(i,2)),'sheet.cell_value(i,1)=',sheet.cell_value(i,1))
                    sales_money += sheet.cell_value(i,2)*sheet.cell_value(i,4)
                    count += sheet.cell_value(i,4)
        money_dict[key] = sales_money
        all_sales_money += sales_money
        count_dict[key] = count
        all_count +=  count
        sales_money = 0
        count = 0
    # print(count_dict)
    # 最畅销的衣服
    for key,value in count_dict.items():
        if value == max(count_dict.values()):
            print(f"最畅销的衣服为:{kind_dict()[key]}")

        elif value == min(count_dict.values()):
            print(f"全年销量最低的衣服:{kind_dict()[key]}")
    print()

    #全年的销售总额,每件衣服的销售额占比,每件衣服的销售（件数）占比
    for key,value in money_dict.items():
        money_dict[key] = proportion_count(money_dict[key],all_sales_money)
        print(f"{kind_dict()[key]}的销售占比为:{money_dict[key]}")

        count_dict[key] = proportion_count(count_dict[key],all_count)
        print(f"{kind_dict()[key]}的销售（件数）占比为:{count_dict[key]}")
    print()
    print('全年的销售总额为:',all_sales_money)

#每件衣服的月销售占比
def total_month_sales():
    sales_money = 0
    month_sales = 0
    money_dict = {}
    for sheet in all_sheet:
        kd_dict = mt_kind_dict(sheet)
        for key,value in kd_dict.items():
            for i in range(1,sheet.nrows):
                if value == sheet.cell_value(i,1):
                    sales_money += sheet.cell_value(i,2)*sheet.cell_value(i,4)
            money_dict[key] = sales_money
            month_sales += sales_money
            sales_money = 0
        for key,value in money_dict.items():
            money_dict[key] = proportion_count(money_dict[key],month_sales)
            print(f"{sheet.name}的{kd_dict[key]}的月销售占比为:{money_dict[key]}",end='    ')
        print()
        kd_dict,money_dict= {},{}
#季度种类字典
def quarterly_kind_dict(list):
    kd_dict = {}
    for sheet in all_sheet:
        for i in list:
            if sheet.name == i:
                kd_dict.update(mt_kind_dict(sheet))
    return kd_dict
#每个季度最畅销的衣服
def quarterly_cloth():
    count = 0
    count_dict = {}
    for quarterly_name,month_list in quarterly_dict.items():
        # print(f"{quarterly_name}的种类字典为:{quarterly_kind_dict(month_list)}")
        kd_dict = quarterly_kind_dict(month_list)
        for month in month_list:
            for sheet in all_sheet:
                if sheet.name == month:
                    for key,value in kd_dict.items():
                        for j in range(1, sheet.nrows):
                            if value == sheet.cell_value(j, 1):
                                count += sheet.cell_value(j,4)
                        if key not in count_dict:
                            count_dict[key] = count
                        else:
                            count_dict[key] += count
                        count = 0

        for key,value in count_dict.items():
            if value == max(count_dict.values()):
                print(f"{quarterly_name}最畅销的衣服为:{kd_dict[key]}")
        count_dict = {}

total_annual_sales()
print()
total_month_sales()
print()
quarterly_cloth()

