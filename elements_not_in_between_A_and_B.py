n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
l2=[]
for i in range(a,b+1):
    l1.append(i)
for i in l:
    if i not in l1:
        l2.append(i)
if len(l2)>0:
    print(*l2)
else:
    print(-1)