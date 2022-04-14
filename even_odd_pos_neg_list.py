a=[2,3,4,5,6,-5,-4,-3,-1,9,8,7]
size=len(a)
count=0
count1=0
count2=0
count3=0
i=0
while i<size:
    if a[i]%2==0:
        count=count+1
    else:
        count1=count1+1
    if a[i]>0:
        count2=count2+1
    else:
        count3=count3+1    
    i=i+1    
print("postive=",count2,)
print("negtive=",count3,)   
print("total even=",count)
print("total odd=",count1)

# a=[-1,-2,-3,-4,-5,-5-6,2,3,4,5,7,8,9]
# size=len(a)
# count=0
# count1=0
# i=0
# while i<len(a):
#     if a[i]%2!=0:
#         count=count+1
#     else:
#         count1+=1
#     if a[i]>0:
#         print("postive=",a[i])
#     else:
#         print("negetive=",a[i]) 
#     i=i+1
# print("total even=",count)
# print("total odd",count1)   
