#This Program will do read the file, Append or write the file, and override the file content.

f1 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "r") #Read The File
print(f1.read())
f1.close()

f2 = open("/home/webmob/Krunal_Work_space/temp/home.txt", "a") #Append data end of the File.
f2.write("\n#comment")
f2.close()

f3 = open("/home/webmob/Krunal_Work_space/temp/home1.txt", "w") #Write the on the file. This is do override the filr content.
f3.write("<Doctype!>")
f3.close()
