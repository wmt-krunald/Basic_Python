#This name function take input from user and greeting.
def wel_user():
    na1 = input("Enter Your Name : ")
    print("Welcome " + na1 + ", in world of Python\n")

wel_user()

#This uname function already pass the argument.
def uname(name, age):
    print("Welcome " + name + ", Your age is " + str(age) + "." )

uname("Krunal", 21) # In above we write str(age) instead of this we can write in calling function time
uname("Mayur", 25)    #... uname("Krunal", "21"). this 21 is consider as a string.