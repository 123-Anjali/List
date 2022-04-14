# l=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# prod=1
# while i<len(l):
#     if i<5:
#         sum=sum+l[i]
#     else:
#         prod=prod*l[i]
#     i=i+1
# print(sum)
# print(prod)



# a=["a","b","c","d"]
# b=["e","f","g","h"]
# c=[1,2,3,4]
# i=0
# e=len(a)
# while i<len(a):
#     print([a[i]+b[i]+str(c[i])])
#     i=i+1



a=["a","b","c","d"]
b=["e","f","g","h"]
i=0
e=len(a)
while i<len(a):
    print([a[i]+b[i]],end=" ")
    i=i+1
a=["a","b","c","d","e","f"]
b=["g","h","i","j","k","l"]
i=0
while i<len(a):
    j=1
    while j<=len(b):
        print([a[i]+b[-j]],end=" ")
        j=j+1
        i=i+1




# a="anjali","singh","chauhan","is","the","studen","of","navgurukul"
# i=0
# while i<len(a):
#     j=1
#     while j<=len(a):
#         print(a[-j],end=" ")
#         j=j+1
#         i=i+1
# i=1
# b=[]
# while i<=len(a):
#     j=1
#     sum=" "
#     while j<=len(a[-i]):
#         sum+=a[-i][-j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)



l=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(l):
    if l[i]%2==0:
        b.append(l[i])
    i=i+1
print(b)
l=b[((len(b)-10)//2)] 
print(l)  





    
    



# i=0
# while i<=60:
#     i=2*i+1
#     print(i)


# a="anjali"
# i=0
# b=[]
# while i<len(a):
#     j=0
#     x=5
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j=j+1
#     x=x+5
# print(b)