import os
import os.path
import datetime


L = {}
k = {}
rootdir = "E:\\根目录\\"
def getdirsize(dir):
    size = 0
    for parent,dirnames,filenames in os.walk(dir):#当一个目录（文件夹同）既有文件又有目录，用os。walk
        for filename in filenames:
            try:
                #用于路径拼接文件路径
                name =  os.path.join(parent,filename)#不用添加dirnames，否则不会执行，即不要中间部分
                # print(name)
                size +=os.path.getsize(name)
            except:
                continue
    return size
def getsizenames(size):
    if(size > 1024*1024*1024.0):
        numstr = str(size/(1024*1024*1024.0))
        sizename = numstr[:(numstr.index('.')+3)]+'GB'
    elif(size > 1024*1024.0):
        numstr = str(size / (1024 * 1024.0))
        sizename = numstr[:(numstr.index('.') + 3)] + 'MB'
    elif(size > 1024.0):
        numstr = str(size / 1024.0)
        sizename = numstr[:(numstr.index('.') + 3)] + 'KB'#取小数用的
    else:
        sizename = str(size)+'Bytes'
    return sizename
starttime = datetime.datetime.now()

filenames = os.listdir(rootdir)
for filename in filenames:
    fullpath = os.path.join(rootdir,filename)
    if os.path.isdir(fullpath):        #用于判断对象是否为一个目录
        L[filename] = getdirsize(fullpath)#自定义函数
    else:
        L[filename] = os.path.getsize(fullpath)
k = sorted(L.items(),key=lambda L:L[1],reverse=True)#true降序
# print(k)
endtime = datetime.datetime.now()
print('\n%s 目录下共有%d个文件（文件夹）'%(rootdir,len(k)))
print('\n共花费了%d秒对文件夹中的文件进行降序排列.结果如下:\n'%(endtime-starttime).seconds)
for i in range(len(k)):
    print(k[i][0],'\t',getsizenames(k[i][1]))
