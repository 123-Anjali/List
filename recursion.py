from pickletools import read_unicodestring1


def sum(number):
    if number==1:
        return 1
    return 2 * sum(number-1)

index=1
while(index<10):
    print(sum(index))
    index+=1



def febo(a):
    if a==1:
        return 0
    elif a==2:
        return 1
    else:
        return febo(a-1)+febo(a-2)
a=int(input("enter the number"))
i=1
while i<=a:
    print(febo(i))
    i=i+1




