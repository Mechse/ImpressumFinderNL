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

    for link in soup.findAll('a'):
        hyperlink = link.get('href')
        hyper_content = http.getContent(hyperlink)

        if hyper_content is not None:
            print hyperlink
            hyperlink_soup = BeautifulSoup(str(hyper_content), "lxml")

        else:
            hyperlink = domain+hyperlink
            hyper_content = http.getContent(hyperlink)
            try:
                hyperlink_soup = BeautifulSoup(str(hyper_content), "lxml")
            except TypeError:
                print("Can't make soup.")
                continue

        if Regex().searchImprints(hyperlink_soup.prettify()):
            if fh.inFile("somethingFound.txt", hyperlink) == -1:
                fh.writeSomethingFound(hyperlink+"\n")
