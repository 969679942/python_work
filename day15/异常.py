'''
    异常：
        在程序正常运行的过程中出现的不正常情况。异常
    1.如何解决？
        异常的解决！
        三板斧：
            try...(监控代码)...except...（进行异常处理）...finally....(处理比较调转的问题)


'''


li = None

def  getValue(li,index):
    return li[index]
try:
    print(getValue(li,7))
except IndexError:  # 匹配异常
    print("嘻嘻！角标错误就处理完成！") # 具体的处理措施
except TypeError:
    print("嘻嘻！类型异常解决了！")
except Exception:  # 用它来兜底
    print("没关系，我都能处理！")