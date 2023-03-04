import re

message = "12 potatoes bought, 6 flowers sold ,  80 Rupees Earned"
Regex = re.compile(r'[aeiouAEIOU]')
print(Regex.findall(message))