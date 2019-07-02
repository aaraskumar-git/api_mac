import requests
import json
import sys


url_with_mac = \
    "https://api.macaddress.io/v1?apiKey=at_otwvZGo0omriCX8mhgLEblvsEBRKr&output=json&search={}".\
        format(sys.argv[1])
response = requests.get(url_with_mac)
json_res = response.json()
print('Company Name: ',json_res['vendorDetails']['companyName'])
