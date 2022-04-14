l=[12,5,4,6,8,7,9,10,23]
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]<l[j]:
            c=l[i]
            l[i]=l[j]
            l[j]=c
        j=j+1
    i=i+1
print(l)

l=[7,8,9,5,4,3,2,1]
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[i]>l[j]:
            c=l[i]
            l[i]=l[j]
            l[j]=c
        j=j+1
    i=i+1
print(l)

