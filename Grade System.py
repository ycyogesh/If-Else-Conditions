a = int(input("Physics : "))
b = int(input("Chemistry : "))
c = int(input("Biology :"))
d = int(input("Mathematics :"))
e = int(input("Computer :"))

percentage = ((a+b+c+d+e)/500) * 100

if(percentage>=90):
    print("Grade A",percentage,"%")
elif(percentage>=80 and percentage<=89):
    print("Grade B",percentage,"%")
elif(percentage>=70 and percentage<=79):
    print("Grade C",percentage,"%")
elif(percentage>=60 and percentage<=69):
    print("Grade D",percentage,"%")
elif(percentage>=40 and percentage<=59):
    print("Grade E",percentage,"%")
else:
    print("Grade F",percentage,"%")


