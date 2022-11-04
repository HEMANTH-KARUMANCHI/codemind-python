n=int(input())
l=list(map(int,input().split()))
c=0
l1=[]
for i in l:
    if( i==l.count(i)):
        c+=1
        l1.append(i)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
if c==0:
    print(-1)
else:
    print(*l2)