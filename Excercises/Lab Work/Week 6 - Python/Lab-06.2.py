import requests
import json

# 1. Read in HTML page and print
#f = open("carviewer2.html", "r")
#html = f.read()
#print (html)

# 2. Access info using API key
#apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
#url = 'https://api.html2pdf.app/v1/generate'

#data = {'html': html,'apiKey': apiKey}
#response = requests.post(url, json=data)
#print (response.status_code)

# 3. Resturn Data and print to .pdf
#newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
#newFile.write(response.content)

# 6. Get info from Private Repo
url = ''
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()

#print (response.json())

file = open("dataDump", 'w')
json.dump(repoJSON, file, indent=4)