height=int(input("height: "))
increase=int(input("inc: "))
decrease=int(input("dec: "))
distance=0
day=0
while distance<height:
    distance=distance+increase
    if distance>=height:
        day+=1
        print(day)
        exit()
    day+=1
    distance=distance-decrease
print(day)