l=[1,2,3-1,-2,-3,-5,6,7,8,9]
b=[]
c=[]
i=0
while i<len(l):
    if l[i]<0:
        b.append(l[i])
    else:
        c.append(l[i])
    i=i+1
print(b)
print(c)
          