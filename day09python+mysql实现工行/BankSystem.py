from MYSQLTool import MYSQLTool
from UserInfo import UserInfo
tool = MYSQLTool('localhost',3306,'bank','root','','utf8')
HelloBank = '''
        *****************************
        *       中国工商银行          *
        *       账户管理系用          *
        *       V1.0                *
        *****************************
        *1.开户                      *
        *2.取钱                      *
        *3.存钱                      *
        *4.转账                      *
        *5.查询                      *
        *6.退出系统                   *
        *****************************
    '''
class BankSystem:

    #判断账号是否存在
    def account_exist(self,account):
        try:
            sql = "select account,username,password,country,province,street,door,money,registerdate,bankname from user where account = %s"
            result = tool.select(sql,[account])
            return result
        except Exception as e:
            print(e)
    #开户
    def add_infos(self,account,name,pwd,country,province,street,door,money,bankname):
        try:
            sql = "insert into user(account,username,password,country,province,street,door,money,registerdate,bankname) values (%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
            lines = tool.insert(sql,[account,name,pwd,country,province,street,door,money,bankname])
            assert lines,"开户失败：该账户已经存在"
            print('开户成功!')
        except Exception as e:
            print(e)
        finally:
             print('还需要使用其他功能请输入序号！')
    #取款
    def withdrawal(self,account,pwd):
        try:
            result = banksys.account_exist(account)
            assert result,"该账号还未开户,请先开户"
            if result[0][2] == pwd:
                print('登录成功,当前余额为:',result[0][7])
                while True:
                    money = int(input('请输入取款金额:'))
                    if money > result[0][7]:
                        print('取款金额大于当前余额,请重新输入!')
                    else:
                        money = result[0][7] - money
                        break
                sql = "update user set money = %s where account = %s"
                lines = tool.update(sql,[money,result[0][0]])
                assert lines,"取款失败!"
                print('取款成功')
            else:
                print('密码错误,取款失败!')
        except Exception as e:
            print(e)
    #存款
    def deposit(self,account,pwd):
        try:
            result = banksys.account_exist(account)
            assert result,"该账号还未开户,请先开户"
            if result[0][2] == pwd:
                print('登录成功,当前余额为:',result[0][7])
                money = int(input('请输入存款金额:'))
                money = result[0][7] + money
                sql = "update user set money = %s where account = %s"
                lines = tool.update(sql,[money,result[0][0]])
                assert lines,"存款失败!"
                print('存款成功')
            else:
                print('密码错误,存款失败!')
        except Exception as e:
            print(e)
    #查询
    def inquire(self,account,pwd):
        try:
            result = banksys.account_exist(account)
            assert result, "该账号还未开户,请先开户"
            if result[0][2] == pwd:
                print('登录成功,当前账户信息为:',
                      f"账号:{result[0][0]},"
                      f"姓名:{result[0][1]},"
                      f"密码:{result[0][2]},"
                      f"地址:{result[0][3]+result[0][4]+result[0][5]+result[0][6]},"
                      f"余额:{result[0][7]},"
                      f"开户时间:{result[0][8]}",
                      f"开户行:{result[0][9]}")
            else:
                print('密码错误,查询失败!')
        except Exception as e:
            print(e)
    #转账
    def transfer_money(self,account,pwd):
        moneys = 0
        try:
            result = banksys.account_exist(account)
            assert result, "该账号还未开户,请先开户"
            if result[0][1] == pwd:
                print('登录成功,当前余额为:', result[0][7])
                while True:
                    accounts = int(input("请输入转账账号:"))
                    #判断转账账号是否存在
                    lines = banksys.account_exist(accounts)
                    assert lines,"转账账号输入错误,转账失败"
                    money = int(input('请输入转账金额:'))
                    if money > result[0][7]:
                        print('转账金额大于当前余额,转账失败!')
                        break
                    else:
                        moneys = result[0][7] - money
                        break
                #更新转出账户余额
                sql1 = "update user set money = %s where account = %s"
                lines = tool.update(sql1, [moneys, result[0][0]])
                assert lines, "转账失败!"

                #更新转入账户余额,先查余额,在累加转入余额
                sql2 = "select money from user where account = %s"
                results = tool.select(sql2, [accounts])
                money = results[0][7] + money
                sql3 = "update user set money = %s where account = %s"
                line = tool.update(sql3, [money, accounts])
                assert line
                print('转账成功')
            else:
                print('密码错误,取款失败!')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    banksys = BankSystem()
    while True:
        print(HelloBank)
        switch_case = int(input('请选择要使用的功能：'))
        if switch_case == 1:
            uinfo = UserInfo(object, object, object, object, object, object, object, object, object, object)
            uinfo.account =None
            uinfo.name = input('请输入姓名：')
            uinfo.pwd = input('请输入密码：')
            uinfo.country = input('请输入国家：')
            uinfo.province = input('请输入省份：')
            uinfo.street = input('请输入街道：')
            uinfo.door = input('请输入门牌号：')
            uinfo.money = 0
            uinfo.bankname = '北京昌平支行' #开户行默认北京昌平支行
            # banksys = BankSystem()
            banksys.add_infos(uinfo.account,uinfo.name,uinfo.pwd,uinfo.country,uinfo.province,uinfo.street,uinfo.door,uinfo.money,uinfo.bankname)

        if switch_case == 2:
            account = int(input('请输入取款账户:'))
            pwd = input('请输入取款密码:')
            banksys.withdrawal(account,pwd)

        if switch_case == 3:
            account = int(input('请输入存款账户:'))
            pwd = input('请输入存款密码:')
            banksys.deposit(account,pwd)

        if switch_case == 4:
            account = int(input('请输入账户:'))
            pwd = input('请输入密码:')
            banksys.transfer_money(account, pwd)

        if switch_case == 5:
            account = int(input('请输入要查询的账户:'))
            pwd = input('请输入账户密码:')
            banksys.inquire(account, pwd)

        if switch_case == 6:
            print('退出成功！')
            break



