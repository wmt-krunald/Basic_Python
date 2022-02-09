#This is kD translator.
#All vowels which are in lower letter a,e,i,o,u will convert in k.
#All vowels which are in upper letter A,E,I,O,U will convert in D.

def tranSlate(word):
    transmission = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transmission = transmission + "D"
            else:
                transmission = transmission + "k"
        else:
            transmission = transmission + letter
    return transmission


print(tranSlate(input("Enter Any Word :")))
    