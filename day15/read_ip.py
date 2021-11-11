'''
读取服务器日志,筛选记录连接最多的IP
'''
f = open(file="baidu_x_system.log",mode='r',encoding='utf-8')

list = f.readlines()

find = {}
for i in list:
    str = i.split(" ")[0]
    if str not in find:
        find[str] = 1
    else:
        find[str] += 1

print(find)