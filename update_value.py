l=[1,2,3,4,5,6,7,8,9,10]
i=0
c=0
b=[]
while i<len(l):
    if c%3==0:
        l[i]=4
        b.append(l[i])
    else:
        b.append(l[i])
    c=c+1
    i=i+1
print(b)