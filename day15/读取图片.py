f = open(file="白冰.jpg",mode="rb")  # 读取
f1 = open(file="D:\\白冰1.jpg",mode="wb")

data = f.read()

f1.write(data)

f1.flush()






