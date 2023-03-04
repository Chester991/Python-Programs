import re
spam = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = spam.search('My Phone number is 555-9426')
print(mo.group())