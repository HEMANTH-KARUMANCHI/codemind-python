s=input()
s1=s.split(" ")
v=['a','e','i','o','u']
for i in s1:
    c=0
    for j in i:
        if j in v:
            c+=1
    print(c,end=" ")