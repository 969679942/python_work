import random
def case_print():
    print("***********************")
    print("*   中国农业银行        *")
    print("***********************")
    print("*     1、开户          *")
    print("*     2、存钱          *")
    print("*     3、取钱          *")
    print("*     4、转账          *")
    print("*     5、查询          *")
    print("*     6、再见          *")
    print("***********************")

index = 0
#空字典
bank={}
#'F': {'account': 98835406, 'password': '1', 'country': '中国', 'porvince': '昌平', 'street': '001', 'door': '001', 'money': 0}
bank_name="M73迪迦银行"
#调用的函数元素是一一对应的，不是名称对应
def bank_add(account,username,password,country,province,street,door):
    if username in  bank:#名字  重名
        return 2
    elif len(bank)>= 100:#大于100个用户
        return 3
    else:#正常添加用户
        bank[username]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1
def Useradd():
    account=random.randint(10000000,99999999)#账号随机产生的
    username=input("请输入您的姓名")
    password=input("请输入你的密码")
    print("下面请输入您的地址：")
    country=input("\t\t请输入你的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    add=bank_add(account,username,password,country,province,street,door)
    if add ==3:
        print("数据库已满，请到光之国银行开户")
    elif add==2:
        print("用户已存在")
    elif add ==1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
#2.存钱
def save_money():
    account = int(input('请输入要存钱的账户：'))
    state = account_exit(account)
    if state:
        print('存钱成功!')
    else:
        print('还未开户')
#3.取钱
def pick_money():
    account = int(input('请输入取钱账号：'))
    password = input('请输入密码：')
    state = take_money(account,password)
    if state == 3:
        print('账号不存在,未开户')

#4.转账
def transfer():
    account = int(input('请输入账号:'))
    password = input('请输入密码：')
    take_money(account,password)




#5.查询
def select_info():
    account = int(input('请输入要查询的账号：'))
    password = input('请输入密码：')
    state = account_pwd(account,password)
    if state:
        print('账号不存在,未开户')

#判断取钱账户和密码以及钱数
def take_money(account,password):
    for username, bank_info in bank.items():
        for key, value in bank_info.items():
            if account == bank_info['account'] and password == bank_info['password']:
                print(f"当前余额：{bank_info['money']}元,")
                if index == 3:
                    money= int(input("请输入取款金额："))
                    if money > int(bank_info['money']):
                        print('取款金额大于当前余额，取款失败')
                    else:
                        balance = int(bank_info['money']) - money
                        bank_info.update({'money':balance})
                        print('取款成功')
                    return 1  # 账号密码正确,取款成功

                if index == 4:
                    account_in = int(input('请输入转账账号:'))
                    state = account_exit(account_in)
                    if state:
                        money = int(input("请输入转账金额："))
                        if money > int(bank_info['money']):
                            print('转账金额大于当前余额，转账失败')
                            return 0
                        else:
                            balance = int(bank_info['money']) - money
                            bank_info.update({'money': balance})
                            for users, bank_ifo in bank.items():
                                for keys, values in bank_ifo.items():
                                    if account_in == values:
                                        bank_ifo.update({'money': (money+bank_ifo['money'])})
                        print('转账成功')
                        return 1
                    else:
                        print('转账账户不存在，转帐失败')

            elif account == bank_info['account'] and password != bank_info['password']:
                print('密码错误')
                return 2
    return 3  # 账号不存在

#判断账户和密码是否正确
def account_pwd(account,password):
    for username, bank_info in bank.items():
        for key, value in bank_info.items():
            if account == bank_info['account'] and password == bank_info['password']:
                    print(f"当前账号：{bank_info['account']},密码:{bank_info['password']},余额：{bank_info['money']}元,",end='')
                    print(f"用户居住地址：{bank_info['country']+bank_info['province']+bank_info['street']+bank_info['door']},",end='')
                    print(f"当前账户的开户行：{bank_info['bank_name']}.")
                    return False #账号密码正确
            elif account == bank_info['account'] and password != bank_info['password']:
                print('密码错误')
                return False
    return True #账号不存在
#判断用户是否存在
def user_exit(username):
    if username in bank:
        return 1
    else:
        return 0

#判断账户是否存在，(当index为2时，存在存钱），返回True，不存在，返回False
def account_exit(account):
    for username, bank_info in bank.items():
        for key,value in bank_info.items():
            if account == value:
                if index == 2:
                    money = input('请输入要存的金额')
                    bank_info.update({'money':money})
                return True
    return False

if __name__ == '__main__':

    while True:
        case_print()
        index=int(input("请输入您的操作"))

        if index == 1:
            Useradd()
            print(bank)
        if index == 2:
            save_money()
        if index == 3:
            pick_money()
            print(3)
        if index == 4:
            transfer()
        if index == 5:
            select_info()
        if index == 6:
            print('退出成功！')
            break

