import re

lyrics = '12 tomatoes eaten, 6 potato sold , 4 flowers bought, 455 Rupees Earned'
spamRegex = re.compile(r'\d+ \w+')
print(spamRegex.findall(lyrics))