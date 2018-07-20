import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import functions as f

outputFile = open("data.csv", "wb")
outputWriter = csv.writer(outputFile)

websites = ["https://www.coa.nl/"]

types = ["email", "tel", "zip", "city", "street"]

file = open("imprints.txt", "r")

imprints = file.read().splitlines()

for type in types:

    file = open(type+".txt", "r")

    if(type == "email"):
        emails = file.read().splitlines()

    elif(type == "tel"):
        tels = file.read().splitlines()

    elif(type == "zip"):
        zips = file.read().splitlines()

    elif(type == "city"):
        cities = file.read().splitlines()

    elif(type == "street"):
        streets = file.read().splitlines()

website = requests.get(websites[0]).text
mainSoup = bs(website, "lxml")
hyperlinks = mainSoup.select('a')

undersites = list()

for hyperlink in hyperlinks:

    try:
        undersites.append(requests.get(websites[0]+hyperlink['href']).text)
    except:
        continue

for imprint in imprints:

    if mainSoup.find_all(text=imprint) is not None:

            email_out = f.DataFinder(mainSoup, emails)

            if f.IsInFile("data.csv", email_out) is not False:

                outputWriter.writerow([str(websites[0]), email_out])

    for undersite in undersites:

        sideSoup = bs(undersite, "lxml")

        if sideSoup.find_all(text=imprint) is not None:

            email_out = f.DataFinder(sideSoup, emails)

            if f.IsInFile("data.csv", email_out) is not False:

                outputWriter.writerow([str(websites[0]), email_out])
