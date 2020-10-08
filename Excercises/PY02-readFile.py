from bs4 import BeautifulSoup as bs

with open("./Lab Work/Lab 2 - JavaScript/Lab2-JavaScript.html") as fp:
    soup = bs(fp, 'html.parser')

print(soup.prettify())