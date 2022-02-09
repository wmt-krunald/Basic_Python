friends = ["Harsh", "Ankur", "Anuj", "Raj"]

for frd_name in friends:
    print(frd_name)     #This for loop print all frd_name

for name in range(len(friends)):
    print(friends[name])    #This for loop print all frd_name
                            #because len = 0 to 3 and for loop execute 1 by 1 in order.

for i in range(10):
    print(i)            #This for loop print 0 to 9 numbers in order

for i in range(5, 12):
    print(i)            #This for loop print 5 to 11 numbers in order
    
for n in range(6):
    print("\nThis number is ", n) #This print 0 to 5 number

for n in range(1, 6):   #This will print odd and even number
    if n%2 == 0:
        print("This is even number and Number is ", n)
    else:
        print("This is odd number and Number is ", n)
    