n1 = float(input("Enter First Number = "))
op = input("\nEnter Operator : ")
n2 =float(input("\nEnter Second Number = "))

if op == "+":
    print("\nYour Answer is : ", n1 + n2)
elif op == "-":
    print("\nYour Answer is : ", n1 - n2)
elif op == "*":
    print("\nYour Answer is : ", n1 * n2)
elif op == "/":
    print("\nYour Answer is : ", n1 / n2)
elif op == "%":
    print("\nYour Answer is : ", n1 % n2)
else:
    print("\nEnter Valid Operator....!")
