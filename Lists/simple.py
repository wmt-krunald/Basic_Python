employee = ["Harsh", "Krunal", "Riddhi", "Ankur", "Raj"]

#In the list we can also save number and boolean value
list1 = ["Krunal", 35000, True]
print (list1) #print list1 value

print (employee) #Print the employee list element
print (employee[1]) #print index 1 element. Index start from 0.

#modify list element

employee[2] = "Anuj"
print (employee) 

print (employee[1:]) #it will print all element from index 1.
print (employee[1:4]) #it will print index 1, 2, 3. Skip last index. This is called range.

print (employee[-1]) #print from last one.
print (employee[-1:]) #agian print same output. Because -1 then nothing element is there.

