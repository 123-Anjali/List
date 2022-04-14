l=["mom","sis","manny","sanny","aman"]
i=0
b=[]
y=[]
while i<len(l):
    str=l[i]
    j=1
    c=""
    while j<=len(l[i]):
        c=c+l[i][-j]
        j=j+1
    if str==c:
        b.append(c)
    else:
        y.append(c)
    i=i+1
print("this elements is palindrom",b)
print("this elements is not palindrom",y)



l=["mom","dad","rani","ravi","121"]
i=0
b=[]
y=[]
while i<len(l):
    str=l[i]
    j=1
    c=""
    while j<=len(l[i]):
        c=c+l[i][-j]
        j=j+1
    if str==c:
        b.append(c)
    else:
        ("nothing")
    i=i+1
print(" palindrom",b)
