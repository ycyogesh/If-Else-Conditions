a = int(input("Enter a Number : "))

if(a%5==0):
    print("Divisible by 5")
    if(a%11==0):
        print("Also Divisible by 11")
elif(a%11==0):
    print("Divisible by 11")
else:
    print("Non-Divisible by 5 and 11")
