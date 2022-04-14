# g=["flour","cheese","carrot"]
# i=0
# while i<len(g):
#     print(g[i])
#     i=i+1

# l=[["g","f","g"],["i","s"],["b","e","s","t"]]
# b=[]
# for i in l:
#     for j in i:
#         print(j,end="")

l=["a","n","a","l","i"]
b=[]
i=0
while i<len(l):
    j=0
    while j<len(l):
        b.append(l[i])
    j=j+1
i=i+1
print(b) 




# l=["a","n","j","a","l","i"]
# b=[]
# for i in l:
#     for j in i:
#         print(j,end="")



l=[1,2,3,4,1,2,3,4]
b=[]
for i in l:
    if i not in b:
        b.append(i)
        print(b)
        product=1
        for i in b:
            product=product*i
            print(product)
 


l=[232,454,345,765,876]
i=0
while i<len(l):
    rev=0
    a=l[i]
    while l[i]>0:
        rev=(rev*10)+l[i]%10
        l[i]//=10
    if a==rev:
        print("palindrom",a)
    else:
        print("not palindrom",a)
    i=i+1


a=[]
size=int(input("how many elements you want enter"))
for i in range (size):
    v=int(input("entr the number"))
    a.append(v)
print(a)
sum=0
for i in range (size):
    sum=sum+a[i]
    print("sum of list elements=",sum)



