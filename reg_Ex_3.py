#Ignoring Spaces
import re
x = 'From: Using the: character'
y = re.findall('^F\S+:',x)
print(y)