#Escape character
import re
x = 'abca049589 skd02'
y = re.findall('[a-z0-9]',x)
print(y)