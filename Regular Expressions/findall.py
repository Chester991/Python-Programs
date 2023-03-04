import re

message = input()
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex.findall(message))