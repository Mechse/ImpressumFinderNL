import db
import http
from regex import Regex
from bs4 import BeautifulSoup
from files import FileHandler

fh = FileHandler()
domains = db.getURLs(10)
for domain in domains:
    content = http.getContent(domain)

    try:
        soup = BeautifulSoup(str(content), "lxml")
    except TypeError:
        print("Can't make soup.")
        continue

    if Regex().searchImprints(soup.prettify()):
        if fh.inFile("somethingFound.txt", domain) == -1:
            fh.writeSomethingFound(domain+"\n")

    for link in soup.find_all('a'):
        print link.get('href')
