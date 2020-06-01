def StringNum():
    digitnum,alphanum = 0,0
    a = input('请输入一串字符：')
    for i in a:
        if i.isdigit():
            digitnum+=1;
        elif i.isalpha():
            alphanum+=1
        else:
            print("该字符串中含有非数字或字母！统计结果错误.")
            break
    return (digitnum,alphanum)
s = StringNum()
print('数字个数：{m}个，字符个数：{n}个'.format(m=s[0],n=s[1]))
