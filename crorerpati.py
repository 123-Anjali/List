l=[600000,324990909,90990900,30000,5600000,690909090,31010101,532010,5104100]
i=0
c=0
c1=0
c2=0
while i<len(l):
    if l[i]>10000000:
        c=c+1
    elif l[i]>1000000:
        c1=c1+1
    elif l[i]>10000:
        c2=c2+1    
    i=i+1
print("crorepat=",c)
print("lakhpati=",c1)
print("dilwale=",c2,l[i])


