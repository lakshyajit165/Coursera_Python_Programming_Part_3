# Libraries used to grab the URL web stuff and import json
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
# service URL for Google Maps API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
if len(address) < 1: exit()

# Concatenate the serviceurl and urllib.parse.urlencode
# which give a dictonary of address equal and this bit
# right here
url = serviceurl + urllib.parse.urlencode(
    {'address': address})

print('Retrieving', url)

# urlopen() to get a handle
uh = urllib.request.urlopen(url)
# Read the whole document in UTF-8
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Load internal strings
try:
    js = json.loads(data)
except:
    js = None
# If false then quit and print data
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()


# Call json dump and print it with an indent of four
#print(json.dumps(js, indent=4))

# Parsing and printing
place_id = js["results"][0]["place_id"]
print('Place id',place_id)