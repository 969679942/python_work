# 有一个列表，[“北京”,”上海”,”广东”]
# 1)将中国所有省会城市添加到上述列表中
#
# 2)广东成为第二大发达城市，将广东排在上海前面
# 1.删除广东   li.remove(“广东”)
# 2.添加  li.insert(1,”广东”)
#
# 3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
def provincial():
    listProvincial = ["北京","上海","广东",'天津市','重庆市','黑龙江省','辽宁省','吉林省','河北省','河南省','湖北省','湖南省','山东省','山西省','陕西省',
                    '安徽省','浙江省','江苏省','福建省','海南省','四川省','云南省','贵州省','青海省',
                    '甘肃省','江西省','台湾省','内蒙古自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','广西壮族自治区','香港特别行政区','澳门特别行政区']

    for i in range(listProvincial.__len__()):
        if listProvincial[i] == '广东':
            listProvincial.remove(listProvincial[i])
        elif listProvincial[i] == '上海':
            listProvincial.insert(i,'广东')
            print(listProvincial)
            break

    list1 = [36710.36, 35427.10, 29863.23, 29667.39, 27665.36, 27650.45, 27620.38, 25369.20]
    sums = 0
    for j in range(len(list1)):
        sums += list1[j]
    print(f'GDPz总和为：{round(sums,2)}，平均GDP为：{round(sums/len(list1),2)}')



#有以下一个列表，求其中是5的倍数的和
def sumMultipleIs5():
    a = [1,5,21,30,15,9,30,24]
    sums = 0
    for i in range(len(a)):
        if a[i]%5 == 0: # 3%2 取余数 为1
            sums += a[i]
            print(a[i])
    print('是5的倍数的和为：',sums)
# 有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）可以选做
# list = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]
#冒泡排序
def pop_list():
    list = [1,2,3,4,5,6,7,8,9]
    for i in range(len(list)):
        for j in range(1,len(list)-i):
            if list[j-1] < list[j]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
    print(list)
    #如果是单纯的数组翻转,可以利用python中负索引
    list.reverse() #无返回值，直接改变列表
    print(list)


# 请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
def ArryCount():
    # 将列表除重，放到新的列表里，从新列表里拿出在旧列表里查询出现的次数
    List = [1, 4, 7, 5, 8, 2, 1, 3, 4, 5, 9, 7, 6, 1, 10]
    List1 = sorted(set(List),key=List.index)
    for i in range(len(List1)):
        iCount = List.count(List1[i])
        print(f'数字{List1[i]}出现的次数为：{iCount}次',end=' ')
    print()
    #利用字典的特性
    languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp',
                 'c', 'javascript', 'java', 'python','matlab', 'python', 'go', 'java']
    stat = {}
    for language in languages:
        if language not in stat:
            stat[language] = 1
        else:
            stat[language] += 1
    print(stat)
ArryCount()