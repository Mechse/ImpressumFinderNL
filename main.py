import requests
from bs4 import BeautifulSoup as bs
import csv
import functions as f
import db

websites = db.GetDomains("SELECT * FROM host WHERE name!='' ORDER BY id LIMIT 100")

imprints = f.FileOpener("imprints")

filesData = {
                "email": f.FileOpener("email"),
                "tel": f.FileOpener("tel"),
                "zip": f.FileOpener("zip"),
                "city": f.FileOpener("city"),
                "street": f.FileOpener("street"),
            }

prefixes = f.FileOpener("prefix")

for website in websites:

    try:

        mainsite = requests.get(website).text

    except:

        try:

            mainsite = requests.get("http://"+website).text

        except:

            try:

                mainsite = requests.get("https://"+website).text

            except:

                continue

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

                emails_out = f.OutputCollector(filesData["email"], mainSoup, emails_out)
                tels_out = f.OutputCollector(filesData["tel"], mainSoup, tels_out)
                zips_out = f.OutputCollector(filesData["zip"], mainSoup, zips_out)
                cities_out = f.OutputCollector(filesData["city"], mainSoup, cities_out)
                streets_out = f.OutputCollector(filesData["street"], mainSoup, streets_out)

        for undersite in undersites:

            newLine = list()

            sideSoup = bs(undersite, "lxml")

            if sideSoup.find_all(text=imprint) is not None:

                    emails_out = f.OutputCollector(filesData["email"], sideSoup, emails_out)
                    tels_out = f.OutputCollector(filesData["tel"], sideSoup, tels_out)
                    zips_out = f.OutputCollector(filesData["zip"], sideSoup, zips_out)
                    cities_out = f.OutputCollector(filesData["city"], sideSoup, cities_out)
                    streets_out = f.OutputCollector(filesData["street"], sideSoup, streets_out)

    emails_out = f.DistinctList(emails_out)

    with open("data.csv", "a") as outputFile:

        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([website, emails_out, tels_out, zips_out, cities_out, streets_out])
