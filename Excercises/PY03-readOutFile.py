from bs4 import BeautifulSoup as bs

with open("./Lab Work/Lab 2 - JavaScript/Lab2-JavaScript.html") as fp:
    soup = bs(fp, 'html.parser')

#print (soup.tr)
rows = soup.findAll("tr")
for row in rows:
    #print("-----------")
    #print(row)
    dataList = []
    cols = row.findAll("td")
    for col in cols:
        dataList.append(col.text)
    print (dataList)