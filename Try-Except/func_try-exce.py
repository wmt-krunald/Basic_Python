try:

    n1 = int(input("\nEnter Any Number : "))
    print(n1)

except ValueError:
    print("\nInvalid Input")


try:
    i = 100 / 0

except ZeroDivisionError as err:
    print(err)
