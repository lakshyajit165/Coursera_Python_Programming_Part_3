import re
x = 'From lakshyajit@gmail.com Sat Jun 19:03 2018'
y = re.findall('From (\S+@\S+)',x)
print(y)