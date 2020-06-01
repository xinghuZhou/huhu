print("读取的内容为:\n")
with open (r'C:\Users\86152\Desktop\text.txt',encoding='gbk') as f:
    for line in f:
        print(line)
print('----------------\n写入后读取的内容:\n-------------\n')
with open(r'C:\Users\86152\Desktop\text.txt','a') as ff:
    ff.writelines(['\n','赶紧开学','！！！'])
with open (r'C:\Users\86152\Desktop\text.txt',encoding='gbk') as f:
    for line in f:
        print(line.rstrip() )
