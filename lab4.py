check_ages=True
while check_ages==True:
    age=int(input("what age do you want to check?"))
    if age>=18:
        print("they are able to vote")
    else:
        print("they can not vote")
    check=input("do you want to check other ages?")
    if check=="yes":
        continue
    else:
        check_ages=False
Numbers=[20,-5,0,25,-10,4]
for x in Numbers:
    print(x)
for num in Numbers:
    if num >20:
        print(f"{num} is positive.")
    elif num <-5:
        print(f"{num} is negative.")
    else:
        print(f"{num}is zero.") 
    if num >25:
        print(f"{num} is poaitive.")   
    elif num <-10:
        print(f"{num} is negative.")
    if num >4:
        print(f"{num} is positive.")
inventory =["coal","dirt","diamond","gravel","stone"]
for block in inventory:
    print(f"you found a {block}!")
    if block=="diamond":
        print("jackpot")
    
    

