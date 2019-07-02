
# api_mac
querying an api with mac address to get its company name
This program has been written in python3
Importing requests module
send mac address in the sys.argv
sys.argv[1] is taken as mac address and send to the requests url
requests url has api-key, search and the output format we require
Parse the response to get the companyName
