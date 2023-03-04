def isPhoneNumber(text) :
    if len(text) != 12 :
        return False
    for i in range(0,3) :
        if not text[i].isdecimal() :
            return False
    if text[3] != '-' :
        return False
    for i in range(4,7) :
        if not text[i].isdecimal() :
            return False 
    if text[7] != '-':
        return False
    return True

message = input()
foundnumber = False
for i in range(len(message)) :
    chunk = message[i:i+12]
    if isPhoneNumber(chunk) :
        print('Phone Number Found: '+ chunk)
        foundnumber = True
if not foundnumber :
    print('Could not find any phone number')