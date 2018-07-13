import db
import http
from bs4 import BeautifulSoup


domains = db.getURLs(10)
for domain in domains:
    content = http.getContent(domain)
    soup = BeautifulSoup(content, "lxml")
    print(soup.prettify())
    break
