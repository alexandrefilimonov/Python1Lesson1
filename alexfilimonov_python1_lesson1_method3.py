import math
a = int(input("Enter first number a:"))
b = int(input("Enter second number b:"))
c = int(input("Enter third number c:"))
if  (b*b-4*a*c)<0 :
    print("There are no solutions!")
else :
    x1 = (-1*b+math.sqrt(b*b-4*a*c))/2*a
    x2 = (-1*b-math.sqrt(b*b-4*a*c))/2*a
    print("The roots are",x1,"and", x2)