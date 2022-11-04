n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if(i==l.count(i)):
        l1.append(i)
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(len(l2))