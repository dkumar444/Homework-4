# Dhanesh kumar 
# 2045141

age = 0

mylist=[]
temp = ""

while temp!="-1":
    temp  = input()
    if temp!="-1":
        mylist.append(temp)

for item in mylist:
    temp = item.split(" ")
    age = temp[1]
    inputName = temp[0]
    try:
        age = int(age)
        print(f"{inputName} {(age + 1)}")
    except ValueError as ve:
        print(f"{inputName} 0")
