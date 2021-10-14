'''
有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
'''
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]

#统计每个人的平均薪资
def average_salary():
    sum = 0
    for i in range(len(names)):
        sum += names[i][5]
    print(f'平均薪资为：{sum/len(names)}')

#统计每个人的平均年龄
def average_age():
    age = 0
    for i in range(len(names)):
        age += names[i][1]
    print(f'平均薪资为：{age / len(names)}')

#公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
def add_names():
    #拆入到列尾，append
    #插入到指定位置，insert
    names.insert(0,['刘备','45','男','220','alibaba',500,'30'])
    # print(names)
#统计公司男女人数
def statistics_number():
    add_names()
    grils,boys = 0,0
    for i in range(len(names)):
        if names[i][2] == '女':
            grils += 1
        if names[i][2] == '男':
            boys += 1
    print(f"公司男生人数为:{boys},女生人数为：{grils}")

#统计每个部门的人数
def department_number():
    add_names()
    number_dict = {}
    #两种方法：1.先除重再遍历累加 2.利用字典的特性 if 元素  not in dict：
    for i in range(len(names)):
        if names[i][6] not in number_dict:
            number_dict[names[i][6]] = 1
        else:
            number_dict[names[i][6]] +=1
    print('各部门人数为：',number_dict)

department_number()

