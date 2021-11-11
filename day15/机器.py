


try:
    print("机器正常启动！")
    # raise SystemError("系统发动机丢失错误！")
    print("机器正常运行！")

except Exception  as e:
    print("异常解决了！",e.args)
finally:  # 不管是否有异常，都必须执行
    print("机器正常关闭！")







