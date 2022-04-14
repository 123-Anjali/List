# a=["Anjali Singh Chauhan"]
# i=0
# coun=0
# coun1=0
# while i<len(a):
#         if a[i]>="A"and a[i]<="Z":
#             coun=coun+1
#         else:
#             coun1=coun1+1
#         i=i+1
# print("upper case",coun)
# print("lower case",coun1)


    
n=["The Quick Brown Fox"]
str=" "
i=0
while i<len(n):
    str=str+n[i]
    i=i+1
p=str.split()
c=0
c1=0
i=0
while i<len(p):
    j=0
    while j<len(p[i]):
        if (p[i][j]==p[i][j].upper()):
            c=c+1
        else:
            c1+=1
        j=j+1
    i=i+1
print("capital letter is ",c)
print("small letter is ",c1)







