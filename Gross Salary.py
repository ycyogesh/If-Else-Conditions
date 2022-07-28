#Calculate Gross Salary of an Employee

"""
    Gross Salary = Basic Pay + DA + HRA
    DA = Dearness Allowance
    HRA = House Rent Allowance
"""

a = int(input("Basic Pay : "))
hra = 0
da = 0

if(a<=10000):
    hra = a*0.2
    da = a*0.8
elif(a>10000 and a<=20000):
    hra = a*0.25
    da = a*0.9
else:       #above 200000
    hra = a*0.3
    da = a*0.95

gross = a + hra +da
print("Gross Salary is :",gross)
