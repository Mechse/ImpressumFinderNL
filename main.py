# import db
# import http
from files import FileHandler
# from bs4 import BeautifulSoup

fh = FileHandler()
fh.writeImprintKeys("HelloWorld")
# domains = db.getURLs(10)
# for domain in domains:
#     content = http.getContent(domain)
#     soup = BeautifulSoup(content, "lxml")
#     print(soup.prettify())
#     break
