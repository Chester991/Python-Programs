import re

message = """At the end of the day, it's the small things that matter most.
From a kind smile to a thoughtful gesture, these little acts of kindness can have a big impact on someone's day. 
At the same time, it's important to remember that not all acts of kindness are equal. 
Some require more effort or sacrifice than others,
but each is valuable in its own way."""

Regex = re.compile(r'.at')
print(Regex.findall(message))