import os

print(os.path.join('folder1','folder2','folder3'))
print(os.sep) # prints the value that the join function uses
print(os.getcwd()) # get current directory
os.chdir('/home/ayush/Documents') #change current directory to the one passed inside funtion.
print(os.getcwd())