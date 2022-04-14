l=[10,12,13,14,17,18,19]
number=30
a=[]
i=0
while i<len(l):
    j=1
    while j<len(l):
        if l[i]+l[j]==number:
            a.append([l[i],l[j]])
        j=j+1
    i=i+1    
print(a)