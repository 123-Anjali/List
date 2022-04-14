


l=[3,4,5,6,7,8,91,14]
c=0
c1=0
i=0
a=[]
b=[]
while i<len(l):
    if l[i]%2==0:
        a.append(l[i])
        c=c+1
    else:
        c1=c1+1
        b.append(l[i])
    i=i+1
print("total even=",a,c,"total odd",b,c1,)
    

    
list=["anjali","vaishali","husna"]
i=0
while i<len(list):
    if len(list[i])%2==0:
        print("even",list[i])
    else:
        print("odd",list[i])
    i=i+1
