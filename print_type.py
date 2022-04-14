l=["anjali",1.2,11,12,3.4,"dev",5.7j,8.6j]
i=0
a=[]
b=[]
c=[]
d=[]
sum=0
sum1=0
sum2=0
while i<len(l):
    if type(l[i])==int:
        sum=sum+l[i]
        a.append(sum,int)
    if type(l[i])==str:
        b.append(l[i])
    if type(l[i])==complex:
        sum1=sum1+l[i]
        c.append(sum1,complex)
    if type(l[i])==float:
        sum2=sum2+l[i]
        d.append(sum2,float)
    i=i+1
print(a)
print(b)
print(c)
print(d)   