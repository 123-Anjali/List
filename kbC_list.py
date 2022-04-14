l=[["how many continens are there?"],
["what is the capital of india?"],
["Ng me kaun sa course pdhya jaata hai"]]
ol=[["1.four","2.nine","3.seven","4.eight"],
["1.chandigarh","2.bhopal","3.chennai","delhi"],
["1.software engineering","2.conselling","3.tourism","4.agriculture"]]
solution_list=[3,4,1]
option_list2=[["2.nine","3.seven"],["4.delhi","2.bhopal"],["1.software engineering","3.tourism"]]
print("kaun banega crorerpati [KBC]")
i=0
sum=0
count=0
while i<len(l):
    print(l[i])
    print(ol[i])
    lil=input("you want a lifeline:yes or no")
    if lil=="yes":
        if count==0:
            print(option_list2[i])
            ans=int(input("choose the option"))
            if ans==solution_list[i]:
                sum=sum+1000
                print("correct answer")
                print("u win RS/-",sum)
                count=count+1
            elif ans!=solution_list[i]:
                print("incorrect answer")
                break
        else:
            print("you dont have lifeline")
            ans=int(input("choose the option"))
            if ans==solution_list[i]:
                sum=sum+2000
                print("entered corect answer")
                print("u win RS/-",sum)
    else:
        ans=int(input("choose the option"))
        if ans==solution_list[i]:
            sum=sum+2500
            print(" correct answer")
            print("u win RS/-",sum)
        elif ans!=solution_list[i] :
            print("incorrect answer") 
            print("lose the game") 
            break
    if i==2:
        if ans==solution_list[i] or ans==solution_list[i]:
            print("congratulation! you won the game")       
    i=i+1