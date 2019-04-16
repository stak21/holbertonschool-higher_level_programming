import urllib.request
import urllib.parse
import sys

values = {'email':sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
        print("Your email is: {}".format(response.read().decode("utf-8")))
