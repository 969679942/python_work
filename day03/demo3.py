#实现输入10个数字，并打印10个数的求和结果
def input_sum():
    sum = 0
    for i in range(1,11):
        try:
            number = float(input(f"请输入第%s个数：" %i))
            print(number)
        except:
            print('ValueError: could not convert string to float')
            number = float(input(f'请重新输入第{i}个数字:'))
            print(number)
        sum += number
    print('十个数求和的结果为：',sum)

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
def input_list():
    list1 = []  #将十个数存到数组中，排序算法计算
    sum = 0
    for i in range(1,11):
        try:
            number=float(input(f"请输入第{i}个数："))
            list1.append(number)
            sum += number
            print(number)
        except:
            print('ValueError: could not convert string to float')
            number =float(input(f'请重新输入第{i}个数字:'))
            list1.append(number)
            sum += number
    print(f"最大的数为：{max(list1)},十个数的和为：{sum},平均数为：{sum/10}")
    return list1

#冒泡排序
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
def bubble_sort():
    # list =[3,5,1,7,9,2,4,6,8,10]
    list = input_list()
    for i in range(list.__len__()):
        for j in range(1,len(list)-i):
            if list[j-1] > list[j]:
                # temp = list[j-1]
                # list[j-1] = list[j]
                # list[j] = temp
                # 交换两者数据，这里没用temp是因为python 特性元组。
                list[j - 1], list[j] = list[j], list[j - 1]
    print(list)

#选择排序
#1.选择排序是一种简单直观的排序算法，他的工作原理大致是将后面的元素中最小的元素，一个一个取出按顺序放置
#2.在末排序序列中找到最小元素（最大）元素，存放到排序序列的起始位置
#3.再从剩余末排序元素中继续寻找最小（最大）元素，然后放置到已排序序列的末尾
#4.重复第二步，直到所有的元素均排序完毕
def selection_sort():
    pass


# 使用random模块，如何产生 50~150之间的数
def number_random():
    import random
    number =random.randint(50,150) #包含 50和150
    print(number)

    list = [1,2,3,4,5,6,7,8,9]
    # print(random.sample(list,5)) #随机切片数组，长度为5

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
def judge_triangle():
    segment1 = float(input('请输入三角形的边1：'))
    segment2 = float(input('请输入三角形的边2：'))
    segment3 = float(input('请输入三角形的边3：'))

    if segment1 == segment2 or segment1 == segment3 or segment2 == segment3:
        print(f'以边长为:{segment1} ,{segment2} ,{segment3} 所构成的三角形为等腰三角形')
    if segment1 == segment2 == segment3:
        print(f'以边长为:{segment1} ,{segment2} ,{segment3} 所构成的三角形为等边三角形')
    if segment1 * segment2 == segment3**2 or segment3 * segment2 == segment1**2 or segment1 * segment3 == segment2**2:
        print(f'以边长为:{segment1} ,{segment2} ,{segment3} 所构成的三角形为直角三角形')
    if segment1 + segment2 < segment3 or segment3 + segment2 < segment1 or segment1 + segment3 < segment2:
        print(f'以边长为:{segment1} ,{segment2} ,{segment3} 不能构成三角形')
    else:
        print(f'以边长为:{segment1} ,{segment2} ,{segment3} 所构成的三角形为普通三角形')

# 有以下两个数，只使用+，-号实现两个数的调换。A=56,B=78
def replace(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(a,b)


#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
def login(count): #count 调用时默认为0
    if count >= 3:
        print('三次密码输入错误系统锁定')
    else:
        name = 'root'
        password = 'admin'
        input_name = input('请输入用户名：')
        input_pwd = input('请输入密码：')
        if name == input_name and password == input_pwd:
            print('登录成功！')
        else:
            print('用户名或密码错误！')
            count += 1
            login(count)

#使用while编程实现求1~100以内的数的和！
def sum_100():
    i,sum = 1,0
    while i <= 100:
        sum += i
        i += 1
    print(sum)

#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
def frog():
    frog_climb =0   # 总爬行
    day = 0         # 多少天
    while frog_climb < 20:
        frog_climb += 3
        if frog_climb < 20:
            frog_climb += -2
            day += 1
        else:
            day += 1
            print('青蛙用了', day, '天爬了出来')
    else:
        print('走完while循环之后必走这里')

frog()

