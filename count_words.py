s=list(map(str,input().split()))
v=['a','e','i','o','u']
c=0
for i in s:
    i1=i.lower()
    if((i1[0] in v) and (i1[-1] not in v)):
        c+=1
print(c)