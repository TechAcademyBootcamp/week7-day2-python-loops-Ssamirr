print("Bu proqram istifadəçinin daxil etdiyi rəqəmi eyni sayda hissələrə parçalayaraq onların artan sırada olub olmadığını bildirməlidir")
l=[]
num=input("Musbet eded daxil edin: ")
while not num.isdigit() or  int(num)<0:
    num=input("Musbet eded daxil edin: ")

div=input("Ededi nece yere bolmek isteyirsiniz: ")
while not div.isdigit() or int(div)<0 or len(num)%int(div) != 0:
    div=input("Ededi nece yere bolmek isteyirsiniz: ")
div=int(div)

y=len(num)//div
for i in range(y):
    x=num[i*div : (i+1)*div]
    l.append(x)

for j in range(0,len(l)-1,1):
    if int(l[j])>int(l[j+1]):
        print("Artan deyil")
        exit()
print("Artandir")



