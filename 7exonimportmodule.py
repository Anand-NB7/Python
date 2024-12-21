# circumference of the circle
# formula for circumference of the circle is c=2*pi*r


import math
radius=float(input("Enter the radius of the circle :"))
circumference=2*math.pi*radius

print(f"The circumference is {circumference}")
#print(f"The circumference is : {round(circumference,2)}") #it will rounds of the decimal digit to 2 figure

# finding the area of the circle
area=math.pi*pow(radius,2)
#print(f"The area of the circle is :{area} ")
print(f"The area of the circle is :{round(area,2)}")

#finding the hypotenuse of the right angle trianle
# formula is c=a2+b2
A=float(input("enter the side A : "))
B=float(input("enter the side B : "))

C=math.sqrt(pow(A,2)+pow(B,2))
print(f"Side C={C}")
