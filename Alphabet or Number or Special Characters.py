a = input("Enter a Character : ")

if(a>='a' and a<='z') or (a>='A' and a<='Z'):
    print(a," is a Character")
elif(a>='0' and a<='9'):
    print(a,"is a Number")
else:
    print(a,"is a Special Characters")
