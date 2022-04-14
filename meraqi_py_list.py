l1=[2,3,4,5,6,7,8,9,1,33]
l2=[9,8,7,6,5,4,3,2,8]
i=0
a=[]
while i<len(l1):
    if l1[i] not in l2:
        a.append(l1[i]) 
    i=i+1
print(a)