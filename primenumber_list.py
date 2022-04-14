# a=[3,4,5,6,7,8,11,34,56,76,89,99,66]
# l=len(a)
# for i in range (l):
#     c=0
#     for j in range(2,a[i]):
#         if a[i]%j==0:
#             c=1
#     if c==0:
#         print(a[i],"is prime number")  
#     else:
#         print(a[i],"is not prime number")  


l=[3,4,5,6,7,8,9,11,23,45]
b=[]
i=0
while i<len(l):
    a=l[i]
    c=0
    j=1
    while a>=j:
        if a%j==0:
            c=c+1
        j=j+1
    if c==2:
        print("prime number",a)
        b.append(a)
    i=i+1
print(b)
