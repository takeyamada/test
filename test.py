with open('./input.txt') as f:
    l = [s.strip().split(":") for s in f.readlines()]
for i,k in enumerate(l[:-1]):
    l[i][0]=int(k[0])
tmp=[]
m=int(l[-1][0])
l=l[:-1]
l.sort()
ans=""
for i in l:
    if m% i[0]==0:
        ans+=i[1]
if ans=="":
    print(m)
else:
    print(ans)
