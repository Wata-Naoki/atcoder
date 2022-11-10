
# 1:50 2:30 3:40 4:10
a=[x for x in input().split()]
b={}
target = ':'

for i, v in enumerate(a):
  key = v[:v.find(target)]  
  value = v[v.find(':')+len(target):]
  b[key]=int(value)

zval=[]
xkey=[]
i=0

for k, v in b.items():
  if i <= 2:
    zval.append(v)
    xkey.append(k)
  else:
    target=zval.index(min(zval))
    zval[target] += v
    xkey[target] += ',' + k
  i+=1

for i in range(1, 4):
  print('truck_{}:{}'.format(i, xkey[i-1]))