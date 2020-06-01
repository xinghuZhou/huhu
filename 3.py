D1={'郑州':'河南','济南':'山东','合肥':'安徽','南京':'江苏','杭州':'浙江'}
print(D1)
D1['石家庄']='河北'
print(D1)
for k in D1:
	print(k,D1[k])
del D1['济南']
print(D1)
d = D1.get('合肥')
print(d)
D1.pop('合肥')
print(D1)
T = tuple(D1.keys())
print(T)
L = list(D1.values())
print(L)
T1=list(T)
D2=[T1,L]
T2=[[row[i]  for row in D2]  for i in range(4)]
D=dict(T2)
print(D)


