#variables is a container for a value (string,integer,float,boolean)
# a variable behaves as if it was the value it contains

#these are strings
first_name="anand"
print(first_name)
food="pizza"
email="anand@gmail.com"
print(f"hi {first_name}")
print(f"you like {food}")
print(f"your email is {email}")

#integers
age=20 #should not be with in the qoutes
quantity=3
no_of_stdents=30
print(f"you are {age} years old")
print(f"you are buying {quantity} iteams")
print(f"your class has {no_of_stdents} students")

#floats-it is a number which contains a decimal part of a number
price=10.99
gpa=8.5
distance=5.5
print(f"the price is {price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance} km")

#boolean is whether true or false
is_student=True
print(f"are you a student?:{is_student}")

is_stu=False
if is_stu:
    print("you are a student")
else:
    print("you are not a student")

for_sale=True
if for_sale:
    print("that item is for sale ")
else:
    print("that bitem is not for sale ")

is_online=True
if is_online:
    print("you are online  ")
else:
    print("you are offline ")

