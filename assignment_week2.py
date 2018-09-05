import re
file = open('assignment_week2.txt')
sum_all = 0
for line in file:
    y = line.split()
    for i in y:
        x = re.findall('[0-9]+',i)
        for j in x:
            sum_all+=int(j)
print(sum_all)
