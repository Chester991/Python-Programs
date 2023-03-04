import re
message = input()
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
spam = phoneNumberRegex.search(message)
print(spam.group())