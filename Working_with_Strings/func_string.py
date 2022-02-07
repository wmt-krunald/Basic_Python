#Some basic function of string

msg = "WebMob Technologies"
print (msg + " is AWESOME") #add extra string. or concnet 2 string

print (msg.upper()) #convert string into uppercase
print (msg.lower()) #convert into lowercase
print (msg.isupper()) #check string is in uppercase
print (msg.islower()) #check string is in lowercase
print (msg.upper().isupper()) #first convert into uppercase and check for upper case
print (msg.lower().islower()) #first convert into lowercase and check for lower case

print (len(msg)) #print length of string
print (msg[1]) #give the character which is on index 1. The index is started from 0.

print (msg.index("T")) #give character's index

print (msg.replace("WebMob", "WEBMOB")) #replace the string. 