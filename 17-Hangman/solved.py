print("Hangman oyunu klassik tapmaca oyunudur")
answer="Honey-Bee"
answer=answer.lower()
dashspace="__________"
string=""
time=True
l1=[]
l2=[]
alreadyExist=[]
while time:
    dashspace=dashspace.capitalize()
    x=input(f"Enter letter: {dashspace}:")
    x=x.lower()
    while x.isdigit() or len(x)>1 or x in alreadyExist or x=='' or answer.find(x)==-1:
        if  answer.find(x)==-1:
            x=input("This letter is not exist,try another: ")
        if  x.isdigit() or len(x)>1 or x=='':
            
            x=input(f"Enter letter(only): {dashspace}:")
        if  x in alreadyExist:
            x=input("This letter is already exist,try another: ")
        
    alreadyExist.append(x)
    l1=[]
    l2=[]
    for i in answer:
        l1.append(i)
    for j in dashspace:
        l2.append(j)
    for a in range (0,len(l1)):
        if l1[a]==x:
            l2[a]=l1[a]
            dashspace=""
    for element in l2:
        dashspace +=element
        if answer.capitalize()==dashspace.capitalize():
            print("Congralutation!!!\nYou find answer!!!")
            exit()
     
