import os

print(os.getcwd())
newfile = open('sample.txt','w') #as we did not pass adirectory it was automatically created inside current directory
newfile.write('this text was written inside vscode without giving it a directory or location')
# as we did not pass a location this will automatically crate the file in default location
newfile.close()
newfile=open('sample.txt','r')
spam = newfile.read()
print(spam)
newfile.close()

newfile2 = open('sample.txt','a')
newfile2.write('\nthis text was appended')
newfile2 = open('sample.txt')
spam2 = newfile2.read()
print(spam2)
newfile2.close()