import requests
from bs4 import BeautifulSoup as bs
import csv
import functions as f
import db



websites = ["https://www.coa.nl/",
            "http://www.cultuurparticipatie.nl",
            ]

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

for website in websites:

    mainsite = requests.get(website).text
    mainSoup = bs(mainsite, "lxml")
    hyperlinks = mainSoup.select('a')

    undersites = list()

    for hyperlink in hyperlinks:

        try:

            undersites.append(requests.get(website+hyperlink['href']).text)

        except:

            continue

    emails_out = list()
    tels_out = list()
    zips_out = list()
    cities_out = list()
    streets_out = list()

    for imprint in imprints:

        newLine = list()

        if mainSoup.find_all(text=imprint) is not None:

                emails_out = f.OutputCollector(emails, mainSoup, emails_out)
                tels_out = f.OutputCollector(tels, mainSoup, tels_out)
                zips_out = f.OutputCollector(zips, mainSoup, zips_out)
                cities_out = f.OutputCollector(cities, mainSoup, cities_out)
                streets_out = f.OutputCollector(streets, mainSoup, streets_out)

        for undersite in undersites:

            newLine = list()

            sideSoup = bs(undersite, "lxml")

            if sideSoup.find_all(text=imprint) is not None:

                emails_out = f.OutputCollector(emails, sideSoup, emails_out)
                tels_out = f.OutputCollector(tels, sideSoup, tels_out)
                zips_out = f.OutputCollector(zips, sideSoup, zips_out)
                cities_out = f.OutputCollector(cities, sideSoup, cities_out)
                streets_out = f.OutputCollector(streets, sideSoup, streets_out)

    emails_out = f.DistinctList(emails_out)

    with open("data.csv", "a") as outputFile:

        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([website, emails_out, tels_out, zips_out, cities_out, streets_out])
