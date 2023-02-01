import pprint
print('Enter the message you want to want characters for')
message = input()
count={}
for i in message :
    count.setdefault(i,0)
    count[i] = count[i] + 1
pprint.pprint(count)