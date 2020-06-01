import os, glob, time
rootdir = "E:\\根目录\\"
L={}
def search_all_files_return_by_time_reversed(path):
    filenames = os.listdir(rootdir)
    for filename in filenames:
        L[filename] = time.ctime(os.path.getmtime(filename))
    a = sorted(L.items(), key=lambda L: L[1], reverse=True)
    print(a)
    print('根据修改时间排序，结果如下：\n')
    for i in range(len(a)):
        print(a[i][0],'\t',a[i][1])
search_all_files_return_by_time_reversed(rootdir)
