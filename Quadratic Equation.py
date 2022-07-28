#Find roots of a Quadratic Equation

"""
    Quadratic Equation = ax^2 + bx + c , a!=0
    No real roots -----> Imaginary roots (Complex)
    One real root -----> Roots are real & same
    Two real roots ----> Roots are real and different

    Discriminant(D) ===> b^2 - 4ac

    X = -b + or - root of b^2 - 4ac / 2a
    
"""

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if(a!=0):
    print("Quadratic Equation----> ax**2 + bx + c")
    d = b**2-(4*a*c)
    d1 = (d**0.5)/2*a
    root1 = +b + d1
    root2 = -b + d1

    if d>0 :
        print("Roots are real & different ",root1,root2)
    elif d==0 :
        print("Roots are real & same ",root1,root2)
    else:
        print("Roots are Imaginary ",root1,root2)
else:
    print("Enter valid Input!")
