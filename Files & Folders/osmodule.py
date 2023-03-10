import os

print(os.path.join('folder1','folder2','folder3'))
print(os.sep) # prints the value that the join function uses
print(os.getcwd()) # get current directory
os.chdir('/home/ayush/Documents')#change current directory to the one passed inside funtion.
print(os.getcwd())# prints current working directory
os.chdir("/home/ayush/OOP Unacademy")# change current directory to one passed inside 
print(os.getcwd())