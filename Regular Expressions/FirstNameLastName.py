import re

Name = input()
Regex = re.compile(r'First Name : (.*) Last Name : (.*)')
print(Regex.findall(Name))