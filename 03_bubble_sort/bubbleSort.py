a=[6,5,3,1,8,7,2,4]

for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)