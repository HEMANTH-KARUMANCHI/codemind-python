s=input()
s1=s.split(" ")
s=0
k=0
for i in s1:
    a=list(i)
    s+=ord(max(a))
    k+=ord(min(a))
print(s-k)