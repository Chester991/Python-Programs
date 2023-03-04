import re

message = "12 potatoes bought, 6 flowers sold ,  80 Rupees Earned"
regex=re.compile(r'\D+')
print(regex.findall(message))