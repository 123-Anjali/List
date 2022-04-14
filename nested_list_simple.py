
# l=[1,2,3,[1,2,3],1,2,3]
# i=0
# b=[]
# while i<len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             b.append(l[i][j])
#             j=j+1
#     else:
#         b.append(l[i])
#     i=i+1
# print(b)
      


n=[2,[3,4,5],[7,8,9],1]
i=0
b=[]
while i<len(n):
    if type(n[i])==list:
        j=0
        while j<len(n[i]):
            b.append(n[i][j])
            j+=1
    else:
        b.append(n[i])
    i+=1
print(b)