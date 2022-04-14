cl=["a","n","a","n","s","a","s","s","s","n","h","h","j"]
b=[]
i=0
c=0
c1=0
c2=0
c3=0
c4=0
c5=0
while i<len(cl):
    if cl[i]=="a":
        c=c+1
    if cl[i]=="n":
        c1=c1+1
    if cl[i]=="s":
        c2=c2+1
    if cl[i]=="h":
        c3=c3=1
    if cl[i]=="j":
        c4=c4+1
    if cl[i]=="h":
        c5=c5+1
    i=i+1
b.append(["a",c])
b.append(["n",c1])
b.append(["s",c2])
b.append(["h",c3])
b.append(["j",c4])
b.append(["h",c5])
print(b) 


list=["a","b","c","d","e","f","g","a","a","e","d","c","c","f"]
l=[]
for i in list:
    c=0
    for j in list:
        if i==j:
            c=c+1
    if i not in l:
        l.append(i)
        print([i,c],end="")


