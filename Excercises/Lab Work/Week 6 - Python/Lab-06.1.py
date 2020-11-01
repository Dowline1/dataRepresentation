import json
import requests
from xlwt import *

url = 'http://127.0.0.1:5000/cars'

reponse = requests.get(url)
data = reponse.json()

# Output to Console
#--------------------------------------
# 1a Output returned JSON to screen
#print(data)

#--------------------------------------
# 1b Output cars individually
#for car in data["cars"]:
#    print(car)

#--------------------------------------
# 1c Write returned JSON to file
# Save to a file
#filename = 'cars.json'
#if filename:
    # Writing JSON data
#    with open(filename, 'w') as f:
#        json.dump(data, f, indent=4)

#--------------------------------------
# 1d Write cars to Excel File
#w = Workbook()
#ws = w.add_sheet('cars')
#row = 0;

#ws.write(row,0,"reg")
#ws.write(row,1,"make")
#ws.write(row,2,"model")
#ws.write(row,3,"price")
#row += 1

#for car in data["cars"]:
#    ws.write(row,0,car["reg"])
#    ws.write(row,1,car["make"])
#    ws.write(row,2,car["model"])
#    ws.write(row,3,car["price"])
#    row += 1
#w.save('cars.xls')

#--------------------------------------
# 2 Create Car on server
#dataString = {'reg':'08 C 1234','make':'Ford','model':'Galaxy','price':12324}
#url = 'http://127.0.0.1:5000/cars'

#reponse = requests.post(url, json=dataString)

#print(reponse.status_code)

#--------------------------------------
# 3 Update Car on server
#dataString = {'make':'Ford','model':'Kuga'}
#url = 'http://127.0.0.1:5000/cars/test'

#response = requests.put(url, json=dataString)

#print(reponse.status_code)
#print(reponse.text)

#--------------------------------------
# 4 Delete Car on server

#url = 'http://127.0.0.1:5000/cars/08%20C%201234'
#response = requests.delete(url)
#print(reponse.status_code)
#print(response.text)

#--------------------------------------
# 5a + 5b create spreadsheet of users following andrew, output to file and console
 
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
#print(data)

# Produce in JSON file
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# Write to Excel File
w = Workbook()
ws = w.add_sheet('users')
row = 0;

ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"html_url")
ws.write(row,3,"type")
ws.write(row,4,"site_admin")
row += 1

# data used as no array name provided
for user in data:
    ws.write(row,0,user["login"])
    ws.write(row,1,user["id"])
    ws.write(row,2,user["html_url"])
    ws.write(row,3,user["type"])
    ws.write(row,4,user["site_admin"])
    row += 1
w.save('github_users.xls')