from unittest import  TestCase
from ddt import ddt
from ddt import data
from ddt import  unpack
from BankSystem import BankSystem
from read_excel import get_body
from read_excel import wt_result
bk = BankSystem()

@ddt
class TestBank(TestCase):

    @data(*get_body('bank.xls','Login_Test_Case'))
    @unpack
    def testAddUser(self,a,b,c,d,e,f,g,h,i,j,k):    # 开户
        # a:账户 ,b:姓名 , c: 密码, d: 国家,e:省份 , f:街道 , g: 门牌号, h:金额 , i: 开户行, j:期望结果 , k:写入的指定行
        result = bk.add_infos(a,b,c,d,e,f,g,h,i)

        if result == j:  # 让程序自动将测试结果写到excel表里。
            #其中bank.xls为excel表名,Login_Test_Case为sheet名,k为指定行,10为指定列,写入内容:通过,0为sheet序号为了方便写入利用copy需要copy
            wt_result('bank.xls', 'Login_Test_Case',k,10,'通过',0)
        else:
            wt_result('bank.xls', 'Login_Test_Case',k,10,'不通过',0)
        # 断言
        self.assertEqual(result,j)

    @data(*get_body('bank.xls','Deposit_Test_Case'))
    @unpack
    def testDeposit(self,a,b,c,d,e):                #存款
        result = bk.deposit(a,b,c)
        if result == d:
            wt_result('bank.xls', 'Deposit_Test_Case', e, 4, '通过',1)
        else:
            wt_result('bank.xls', 'Deposit_Test_Case', e, 4, '不通过',1)


    @data(*get_body('bank.xls','Deposit_Test_Case'))
    @unpack
    def testWithdrawal(self,a,b,c,d,e):             #取款
        result = bk.withdrawal(a,b,c)

        if result == d:
            wt_result('bank.xls','Withdrawal_Test_Case',e,4,'通过',2)
        else:
            wt_result('bank.xls', 'Withdrawal_Test_Case', e, 4, '不通过',2)


    @data(*get_body('bank.xls','Transfer_Test_Case'))
    @unpack
    def testTransfer(self,a,b,c,d,e,f):             #转账
        result = bk.transfer_money(a,b,c,d)

        if result == e:
            wt_result('bank.xls','Transfer_Test_Case',f,5,'通过',3)
        else:
            wt_result('bank.xls', 'Transfer_Test_Case', f, 5, '不通过', 3)

    @data(*get_body('bank.xls','Inquire_Test_Case'))
    @unpack
    def testInquire(self,a,b,c,d):                  #查询
        result = bk.inquire(a,b)
        if result == c:
            wt_result('bank.xls','Inquire_Test_Case',d,3,'通过',4)
        else:
            wt_result('bank.xls', 'Inquire_Test_Case', d, 3, '不通过', 4)






