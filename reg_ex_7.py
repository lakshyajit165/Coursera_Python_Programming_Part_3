import re
lin = 'From lakshyajit@gmail.com Sat Jan 12 2017'
y = re.findall('@([^ ]*)',lin)
print(y)