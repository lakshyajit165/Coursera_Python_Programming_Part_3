#extracting email
import re
x = 'From lakshyajit@gmail.com Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)