import re

message = "Agent Robin betrays Agent Batman because of Agent Joker"
Regex = re.compile(r'Agent (\w)\w*')
print(Regex.findall(message))

print(Regex.sub(r'Agent \1', message))