#IF statment example
is_good = False

if is_good:
    print("You are good guy.")
else:
    print("You are bad guy.")


#Another Example

is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both!")
else:
    print("You are not a tall male")

if is_male and is_tall:
    print("You are a tall man")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not male but tall.")
else:
    print("You are not a tall male")