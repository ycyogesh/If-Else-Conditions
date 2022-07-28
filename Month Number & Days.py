#Month number and Month days

n = input("Enter Month Number : ")

if(n=='1' or n=='3' or n=='5' or n=='7' or n=='8' or n=='10' or n=='12'):
    print("31 Days")
elif(n=='4' or n=='6' or n=='9' or n=='11'):
    print("30 Days")
elif(n=='2'):
    print("28 or 29 Days Depending upon leap year")
else:
    print("Enter Correct Number(1-12)")
