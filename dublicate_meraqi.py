l=[19,23,19,13,13,14,14,15,15,18,18,19,18,19,17,17]
b=[]
i=0
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
    i=i+1
print(b)


l=[1,2,3,1,2,3]
b=[]
i=0
while i<len(l):
    if l[i] not in b:
        b.append(l[i])
    i=i+1
print(b)
