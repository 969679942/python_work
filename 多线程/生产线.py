from threading import Thread
from time import sleep
all_tart = 0
basket = 0   #篮子

class Chef(Thread):
    name = ''
    count = 0 #厨师做蛋挞数量
    def run(self) -> None:
        global basket,all_tart
        while True:
            if all_tart >= 6000:
                print(f'厨师:{self.name},做了{self.count}个蛋挞,当天的工资为:{self.count*1.5}')
                break
            else:
                if basket < 500:
                    all_tart += 1
                    self.count += 1
                    basket += 1
                    print(f'厨师:{self.name},做了{self.count}个蛋挞')
                else:
                    sleep(3)
    # def salary(self,count):
    #     print(self.name,"当天的工资为:",count*1.5)


class Customer(Thread):
    username = ''       #姓名
    tart_count = 0      #买的蛋挞数量
    self_money = 3000   #携带现金
    def run(self) -> None:
        global basket
        while True:
            if basket > 0:
                self.tart_count += 1
                basket -= 1
                self.self_money -= 3
                print(f'顾客:{self.username},抢了{self.tart_count}个蛋挞')
                if self.self_money == 0:
                    break
            else:
                sleep(2)


u1 = Chef()
u2 = Chef()
u3 = Chef()
u1.name = '1'
u2.name = '2'
u3.name = '3'
u1.start()
u2.start()
u3.start()


c1 = Customer()
c2 = Customer()
c3 = Customer()
c4 = Customer()
c5 = Customer()
c6 = Customer()
c1.username = 'G1'
c2.username = 'G2'
c3.username = 'G3'
c4.username = 'G4'
c5.username = 'G5'
c6.username = 'G6'
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()