l=[-1,-2,3,4,45,6,5,8,-6,8,-9,-5]
i=0
b=[]
while i<len(l):
    if l[i]>0:
        b.append(l[i])
    i=i+1
print(b)
l=b[((len(b)-1)//2)]
print(l)

