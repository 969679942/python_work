


def getValue():
    try:
        print("hello,jason jia!")
        raise SystemError("蓝屏！")
        return 1
    except Exception:
        return 2
    finally:
        print("我免费了！")
        return 3



print(getValue())
















