hellofile = open('/home/ayush/Documents/plain2.txt','w')#if the file does not exist inside folder it will automatically create one
hellofile.write('This text was written inside VSCode via python')
hellofile = open('/home/ayush/Documents/plain2.txt')
spam2 =  hellofile.read()
print(spam2)
hellofile.close()