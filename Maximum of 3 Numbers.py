a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))
c = int(input("Enter Number 3 :"))

if(a>b and a>c):
    print("A is Greater")
elif(b>c):
    print("B is Greater")
elif(c>a and c>b):
    print("C is Greater")
else:
   pass 
if(a==b and a!=c):
    print("A is Equal to B")
elif(b==c and a!=b):
    print("B is Equal to C")
elif(c==a and c!=b):
    print("C is Equal to A")
else : #(a==b==c)
    print("All are Equal")
