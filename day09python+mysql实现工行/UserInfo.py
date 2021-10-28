import random
class UserInfo:
    '''在python中，封装按照如下步骤进行操作
        (1) 定义类型，所有属性私有化[双下划线开头]
        (2) 每个属性提供set/get方法[赋值/取值]
            命名规范：赋值：set_属性名称(..)
                    取值：get_属性名称(..)
        (3) 在get/set方法中，提供限制条件！
    '''
    # UserInfoCount = 0
    def __init__(self,account,name,pwd,country,province,street,door,money,registerdate,bankname):
        self.__account = account
        self.__name = name
        self.__pwd = pwd
        self.__country = country
        self.__province = province
        self.__street = street
        self.__door = door
        self.__money = money
        self.__registerdate = registerdate
        self.__bankname = bankname
        # self.__UserInfoCount += 1

    @property
    def account(self):
        return self.__account
    @account.setter
    def account(self,account):
        account = random.randint(10000000,99999999)
        self.__account = account

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def pwd(self):
        return self.__pwd
    @pwd.setter
    def pwd(self,pwd):
        self.__pwd = pwd

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self,country):
        self.__country = country

    @property
    def province(self):
        return self.__province
    @province.setter
    def province(self,province):
        self.__province = province

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self,street):
        self.__street = street

    @property
    def door(self):
        return self.__door
    @door.setter
    def door(self,door):
        self.__door = door

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money

    @property
    def registerdate(self):
        return self.__registerdate
    @registerdate.setter
    def registerdate(self,registerdate):
        self.__registerdate = registerdate

    @property
    def bankname(self):
        return self.__bankname
    @bankname.setter
    def bankname(self,bankname):
        self.__bankname = bankname


    # def setAccount(self,account):
    #     self.account = account
    # def getAccount(self):
    #     return self.account
    #     return self.bank_deposit


    def printInfo(self):
        print('账号：',self.account)
        print('姓名：',self.name)
        print('密码：',self.pwd)
        print('地址：',self.country,self.province,self.street,self.door)
        print('存款余额：',self.money)
        print('注册时间：',self.registerdate)
        print('开户行：',self.bankname)


# JSON数据格式：[{'name':'sch','pwd':'123'},{'name':'tdtw','pwd':'456'}]

class Color:
    def __init__(self, rgb_value, name):
        self.__rgb_value = rgb_value
        self.__name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self.__name = name

    def _get_name(self):
        return self.__name

    name = property(_get_name, _set_name)

# if __name__ =='__main__':
#     c = Color('#ff0000', 'bright red')
#     print(c.name)
#     c.name = 'red'
#     print(c.name)
#     userinfo = UserInfo(object,1,1,1,1,1,1)
#     print(userinfo.account)
#     userinfo.account = None
#     print(userinfo.account)