l=[1,2,3,4,5,6,7,8,23,45,67]
m=0
m2=0
m3=0
i=0
while i<len(l):
    j=0
    while j<len(l):
        if l[j]>m:
            m=l[j]
        if l[j]>m2 and l[j]!=m:
            m2=l[j]
        if l[j]>m3 and l[j]!=m and l[j]!=m2:
            m3=l[j]
        j=j+1
    i=i+1
print(m)
print(m2)
print(m3)
