T1 = ('河北','河南','山东','安徽','江苏','浙江','河南','福建')
print(T1)
不能
for s in T1:
	print(s)
i = 0
while i < len(T1):
	print(T1[i])
	i = i + 1
print(T1.count('河南'))
print(T1.index('山东'))
L1 = list(T1)
print(L1)
print(''.join(T1))
T2 = (' 北京 ',' 天津 ',' 上海 ')
T3 = T1 + T2
print(T3)
