#Electricity Bill Calaculation

a = int(input("Enter Unit : "))
amt = 0
total = 0

if(a<=50):
    amt = a*0.50
elif(a<=150):
    amt = 25 + ((a-50)*0.75)
elif(a<=250):
    amt = 100 + ((a-150)*1.20)
else:
    amt = 220 + ((a-250)*1.50)

scharge = amt * 0.20
total = amt + scharge
print("Electricity Bill is :",total)
