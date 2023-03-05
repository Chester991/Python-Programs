import re

message = "Agent Robin betrays Agent Batman because of Agent Joker"
Regex = re.compile(r'Agent')
print(Regex.findall(message))

print(Regex.sub('Hero',message))