a="the quick brown fox jumped over the lazy dag the dog slept over the veradah"
b=a.split(" ")
i=0
while i<len(b):
    if "over" in b[i]:
        b[i]="on"
    i=i+1
print(b) 






a=["my", "name" ,"is", "anjali"]
i=0
b=[]
while i<len(a):
    if a[i]=="is":
        pass
    else:
        b.append(a[i])
    i+=1
print(b)
   
  



            
a=["my","name","is", "anjali"]
i=0
count=0
while i<len(a):
    count=count+1
    i=i+1
print(count)


    



a="my name is anjali"
i=0
coun=0
while i<len(a):
    if a[i]==" ":
        coun=coun+1
    i=i+1
print(coun)

