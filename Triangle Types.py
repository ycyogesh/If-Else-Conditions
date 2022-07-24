a = int(input("Enter Side 1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))

"""
   Equilateral  = 3 sides are Equal
   Isosceles    = 2 sides are Equal
   Scalene      = No sides are Equal
"""
if(a==b==c):
    print("Equilateral")
elif(a==b or a==c or b==a):
    print("Isosceles")
else:
    print("Scalene")


