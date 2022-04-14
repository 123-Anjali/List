# a=[2,4,5]
# print(a)
# a.extend([7,8,9])
# print(a)

# a=[9,8,7,6,5]
# a.append(1)
# print(a)
# c=[2,3]
# a.append(c)
# print(a)

# a=[2,3,4]
# a.insert(0,6)
# print(a)

# b=[1,2,3,4,5,6,7,8,9,]
# b.insert(3,88)
# print(b)

# a=["nish","neha","meena","tina"]
# print("lenth of the list is",len(a))


# l=[8,7,6,5,4,3,2,12]
# l.pop()
# print(l)




a=[[2,3,4],[4,5,6],[7,6,5]]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum+=a[i] 
    i=i+1
print(sum) 



