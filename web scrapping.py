import requests, sys, webbrowser, bs4
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')