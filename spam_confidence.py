import re
file = open('assignment_week2.txt')
output = []
for line in file:
    match = re.search('[0-9]+',line)
    if(match):
        output.append(int(match.group()))
print(sum(output))
