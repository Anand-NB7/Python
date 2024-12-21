#input= a function that prompts the user to enter data
# returns the entered data as a string

name=input("what is ur name?:")
age=input("how old are you?:")
age=int(age) #or u can also use age=int(input(----))
age=age+1
print(f"hello {name} !")
print("happy birthday")
print(f"you are {age} years old ")

#exercise1 area of a rectangle (A=LW)
lenght=float(input("enter the lenght :"))
width=float(input("enter the width :"))
area=lenght*width
print(f"the area of rectangle is :{area} msquare ")#to add a super script numlock+alt+0178

#exercise2 shopping cart program
iteam=input("What iteam would you like to buy? :")
price=float(input("what is the price? :"))
quantity=int(input("How many would you like? :"))
total=price*quantity
print(f"you have bought {quantity}x{iteam}/s")
print(f"The total price is {total} rs")