a = int(input("Enter Side 1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))

"""
    a+b>c
    b+c>a
    c+a>b
"""
if(a+b<c or b+c<a or a+c<b):
    print("Not Valid")
else:
    print("Valid")
