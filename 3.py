valid=['0','1','2','5','6','8','9']
n=int(input())
l=[]
u=1
v=1
while(v<=n):
    str1=str(u)
    x=0
    for i in str1:
        if(i in valid):
            x+=1
    if(x==len(str1)):
        l.append(str1)
        v+=1
    u+=1
f=l[len(l)-1]
f=int(f)
print(f)
