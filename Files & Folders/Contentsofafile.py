helloFile = open("/home/ayush/Documents/plain.txt")
print(helloFile.read())
print(helloFile.read()) #wont work as we can read only once
helloFile.close()

helloFile = open("/home/ayush/Documents/plain.txt")
spam = helloFile.read()
print(spam)
print(spam)