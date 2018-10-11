# Libraries used to grab the URL web stuff and import json
import urllib.request, urllib.parse, urllib.error
import json

input_url = input("Enter the URL: ")

print('Retrieving ', input_url)


uh = urllib.request.urlopen(input_url)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')


sum = 0
count = 0

info = json.loads(data)



#print(info['comments'])

for i in info['comments']:
    #print(i['count'])
    count+=1
    sum+=i['count']
print('Count:',count)
print(sum)



