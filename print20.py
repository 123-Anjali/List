# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# b=[]
# i=0
# c=0
# while i<len(l):
#     b.append(l[i])    
#     if c==3:
#         b.append(20)
#         c=c-4
#     c=c+1
#     i=i+1
# print(b)

   
l=[1,2,3,4,5,6,7,8,9,10]
i=0
c=1
b=[]
while i<len(l):
    if c%3==0:
        l[i]=10
        b.append(l[i])
    else:
        b.append(l[i])
    c=c+1
    i=i+1
print(b)

