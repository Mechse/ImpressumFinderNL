import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import functions as f



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

    for imprint in imprints:

        if mainSoup.find_all(text=imprint) is not None:

                emails_out = f.DataFinder(mainSoup, emails)
                emails_out = f.DistinctList(emails_out)

                if emails_out:

                    for email_out in emails_out:

                        if not f.IsInFile("data.csv", email_out):

                            with open("data.csv", "a") as outputFile:

                                outputWriter = csv.writer(outputFile)
                                outputWriter.writerow([str(website), email_out])

        for undersite in undersites:

            sideSoup = bs(undersite, "lxml")

            if sideSoup.find_all(text=imprint) is not None:

                emails_out = f.DataFinder(sideSoup, emails)
                emails_out = f.DistinctList(emails_out)

                if emails_out:

                    for email_out in emails_out:

                        if not f.IsInFile("data.csv", email_out):

                            with open("data.csv", "a") as outputFile:

                                outputWriter = csv.writer(outputFile)
                                outputWriter.writerow([str(website), email_out])
