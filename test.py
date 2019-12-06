with open('./input.txt') as f:
    l = [s.strip().split(":") for s in f.readlines()]
tmp=[]
m=int(l[-1][0])
l=l[:-1]
l.sort()
ans=""
for i in l:
    if m% int(i[0])==0:
        ans+=i[1]
if ans=="":
    print(m)
else:
    print(ans)
