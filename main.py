import db
import http
from regex import Regex
from bs4 import BeautifulSoup
from files import FileHandler

fh = FileHandler()
domains = db.getURLs(10)
for domain in domains:
    content = http.getContent(domain)
    soup = BeautifulSoup(content, "lxml")
    if Regex().searchImprints(soup.prettify()):
        if fh.inFile("somethingFound.txt", domain) == -1:
            fh.writeSomethingFound(domain+"\n")
