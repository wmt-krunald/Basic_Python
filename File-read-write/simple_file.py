#This is basic of Read and Write File 

# r  - read the file
# w  - write the file (Override the file)
# a  - append data on the file
# r+ - read and write the file 

f1 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "r")
print(f1.readable())  #This will print boolean value
f1.close()

f11 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "r")
print(f11.read())  #This will print the file
f11.close()

f12 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "r")
print(f12.readline())  #This will print the first line of the file
f12.close()

f13 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "r")
print(f13.readlines())  #This will print the list of the file lines
f13.close()

f2 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "w")
print(f2.readable())  #This will print boolean value
f2.close()

f3 = open("/home/webmob/Krunal_Work_space/temp/i1.txt", "r")
for line in f3.readlines():
    print(line)
f3.close()              #This will print file line by line