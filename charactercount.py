import pprint
print('Enter the message you want to want characters for')
message = input()
count={}
for i in message :
    count.setdefault(i,0)
    count[i] = count[i] + 1
for i,j in count.items() :
    print(str('Character '+ str(i) + ' is appearing ' + str(j) + ' times'))
