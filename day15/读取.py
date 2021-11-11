'''
    r:读取
    w:写入
    +:可读可写
    a:附加

    b:byte字节模式


'''
try:
    f = open(file="古诗.txt",mode="r+",encoding="utf-8")

    # data = f.read()  # 全文读取
    # data = f.readline()  一行一行的读
    # data1 = f.readline()
    data = f.readlines() # 将所有行的数据，存在列表中。

    print(data)
except Exception:
    print("文件不存在！别瞎弄！")


