a=[2,3,4,5,6,7,8,9,11,22]
count=0
count1=0
count2=0
sum=0
sum1=0
sum2=0
i=0
while i<len(a):
    sum+=a[i]
    count+=1
    if a[i]%2==0:
        count1=count1+1
        sum1=sum1+a[i]
    else:
        count2=count2+1
        sum2=sum2+a[i]
    i=i+1
print(count1,"=even number")
print(count2,"=odd number")
print(count,"=total number")
print("even sum=",sum1)
print("odd sum=",sum2)
print("total sum=",sum)
print("odd sum=",sum2/count2)
print("even sum=",sum1/count1)
print("total sum=",sum/count)


l=[25,45,13,18,17]
sum=0
i=0
while i<len(l):
    a=str(l[i])
    j=0
    while j<len(a):
        sum=sum+int(a[j])
        j=j+1
    i=i+1    
    print(sum)


ch=[["a","n"],["j","a"],["l","i"]]
i=0
sum=""
while i<len(ch):
    j=0 
    while j<len(ch[i]):
        sum=sum+ch[i][j]
        j=j+1
    i=i+1
print(sum)



l=[1,2,3,4,5]
sum=0
i=0
while i<len(l):
    sum=sum+l[i]
    i=i+1
print(sum)




list=[12,11,123,1212]
i=0
while i<len(list):
    a=str(list[i])
    j=0
    sum=0
    while j<len(a):
        sum=sum+int(a[j])
        j=j+1
    i=i+1    
    print(sum)


