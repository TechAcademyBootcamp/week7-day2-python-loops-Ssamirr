num=input("Enter numbers: ")
odd=0
even=0

while not num.isdigit():
    num=input("Enter numbers: ")

for i in num:
    i=int(i)
    if i%2==0:
        even+=1
    else :
        odd+=1
print(f"even:{even}\nodd:{odd}")
