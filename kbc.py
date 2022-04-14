q=["what is the national flower",
"what is the national animal",
"what is the capital of india"]
option_list=[["1.rose,","2.tulip","3.lotus","4.lily"],
["1.dog","2.cat","3.tiger","4.lion"],
["1.delhi","2.kanpur","3.nagpur","4.bahraich"]]
solution_list=[3,3,1]
option_list2=[["1.rose","3.lotus"],["1.dog","3.tiger"],["1.delhi","2.kanpur"]]
print("kaun banega crorerpati[KBC]")
i=0
sum=0
count=0
while i<len(q):
    print(q[i])
    print(option_list[i])
    lil=input("you want to lifeline yes:or no")
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
                print("you lose the game")
                break
        else:
            print("you dont have lifeline")
            ans=int(input("choose the option"))
            if ans==solution_list[i]:
                sum=sum+200
                print("intered correct answer")
                print("you win RS/-",sum)
    else:
        ans=int(input("choose thr option"))
        if ans==solution_list[i]:
            sum=sum+3000
            print("correct answer") 
            print("you win RS/-",sum)
        elif ans!=solution_list[i]:
            print("incorrect answer")
            print("you lose the game")
            break
    if i==2:
        if ans==solution_list[i]:
            print("congratulation! you won the game")
    i=i+1









