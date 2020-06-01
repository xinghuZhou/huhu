a = input("请输入字符串：")
def zc():
    c = 0
    for s in a:
        if s not in ['0','1','2','3','4','5','6','7','8','9']:
            print("该字符串含有非数字，不能参与计算。")
            c=1
            break
    if c == 1:
        pass
    else:
            b = eval(a)
            if b % 3 == 0 & b % 7 == 0:
                print("该数能被3和7整除！")
            else:
                print("该数不能被3和7整除！")
zc()
