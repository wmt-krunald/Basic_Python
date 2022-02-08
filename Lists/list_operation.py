friends = ["Ramu", "Shamu", "Kaliyo", "Bhuriyo", "Chhotu"]
numbers = [10, 20, 30, 5, 15, 25]

print(len(friends)) #print length of list

print (friends) #print friends list
print (numbers) #print numbers list

#we can append element or list
friends.append("Motu") #append function will take only one parameter and append in last
print(friends)

#To add element in between list
friends.insert(2, "Laliyo") #insert function add element in between list 
print(friends) #and all the other elements are push behind and INSERT IS ALSO TAKE 2 ARGUMENTS 1> INDEX NUMBER 2> STRING NAME

#To remove element 
friends.remove("Laliyo")
print(friends)

#To pop element. Last element is poped out 
friends.pop()
print(friends)

#Check index for an element
print(friends.index("Chhotu"))

#To count the element
friends.append("Ramu")
print(friends.count("Ramu"))

#To sort and reverse the string
friends.sort()
numbers.sort()
print(friends)
print(numbers)

friends.reverse()
numbers.reverse()
print(friends)
print(numbers)

#To copy string
numb = numbers.copy()
print(numb)

#Extend list
friends.extend(numbers)
print(friends) #extend friends list only
print(numbers) #do not extend numbers list