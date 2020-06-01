import os
path = r'E:\根目录'
print('将根目录下的文件夹和文件分开：')
for parent,dirnames,filenames in os.walk(path):
                print(dirnames,filenames)
                break
print("\n根据文件类型列出根目录下所有文件：")
for i in filenames:
                print(i)
