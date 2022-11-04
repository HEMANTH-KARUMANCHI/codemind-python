n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in l:
    if l.count(i)==k:
        l1.append(i)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
if len(l2)>0:
    print(*l2)
else:
    print(-1)