a=input("enter the name")
i=0
while i<len(a):
    if a[i]=="a" or   a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="u":
        print("vowels=",a[i])
    else:
        print("consonent=",a[i])
    i=i+1

l=["a","n","j","a","l","i"]
b=str(l)
i=0
while i<len(l):
    if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u":
        print("vowel=",l[i])
    else:
        print("consonent=",l[i])
    i=i+1