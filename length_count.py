a=[1,2,[1,2,3],[1,2,3],7,8]
i=0
c=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            c=c+1
            j=j+1
    else:
        c=c+1
    i=i+1
print(c)
            

