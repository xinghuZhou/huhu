year = eval(input("请输入一个年份："))
if year%100 == 0 :
                year = year/100
                if year%4== 0:
                                print("该年份为闰年！")
                else:
                                print("该年份不是闰年！")
elif   year%4 ==0:
                print("该年份为闰年！")
else:
                print("该年份不是闰年！")
