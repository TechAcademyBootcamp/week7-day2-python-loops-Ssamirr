string=input("Write: ")
x=string.split()
count_digit=0
count_letter=0
for i in x:
    for j in i:
        if j.isdigit():
            count_digit+=1
        if j.upper()!=j.lower():
            count_letter+=1
print(f"Count-digit:{count_digit}\nCount-letter:{count_letter}")

# import string 
# x=input()
# for i in x:
#     if i in string.digits:
#         count_digit+=1
#     if i in string.ascii_letters:
#         count_letter+=1
# print(f"Count-digit:{count_digit}\nCount-letter:{count_letter}")

