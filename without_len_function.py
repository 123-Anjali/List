l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23]
count=0
for i in l:
    count=count+1
print(count)

from ast import Try


l=[1,2,3,5,6,7,8]
count=0
while True:
    try:
        if l[count]:
            count=count+1
    except IndexError as e:
        break
print(count)






    







s=input("enter a string")
print("string length is:",len(s))


    
