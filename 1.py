L1 = ['北京','上海','天津','济南','郑州','合肥','南京','杭州']
print(len(L1))
L1.append('福州')
print(L1)
L1.insert(3,'太原')
print(L1)
L1[2]='石家庄'
print(L1)
L1.remove('上海')
print(L1)
s = L1.pop(0)
print(s)
print(L1)
s = L1.index('郑州')
print(s)
print(L1[0:5])
print(L1[:6])
print(L1[5:])
L1.reverse()
print(L1[3:])
for n in L1:
	print(n)
	i = 0
while i < len(L1):
	print(L1[i])
	i = i+1
T = tuple(L1)
print(T)
L = [[1,2,3,4,5,6,7,8],L1]
L2 = [[row[i] for row in L] for i in range(8)]
print(L2)

