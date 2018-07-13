import db
import http
from regex import Regex
from bs4 import BeautifulSoup


domains = db.getURLs(10)
for domain in domains:
    content = http.getContent(domain)
    soup = BeautifulSoup(content, "lxml")
    if Regex().searchImprints(soup.prettify()):
        print domain
