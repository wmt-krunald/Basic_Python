#This is Exponent example or raise to power example using #For Loop

base_num = int(input("\nEnter Your Base Number :"))
power_num = int(input("\nEnter Your Power Number :"))

def raise_to_power(base_num, power_num):
    result = 1
    for i in range(power_num):
        result = result * base_num
    return result

print("\nYour Answer is : ", (raise_to_power(base_num, power_num)))