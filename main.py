import db
import http

domains = db.getURLs(10)
for domain in domains:
    content = http.getContent(domain)
    print(content+"\n\n")
