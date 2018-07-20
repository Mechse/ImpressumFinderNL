import re
import csv


def IsInFile(file, finder):

    with open(file, "r") as f:

        reader = csv.reader(f)

        for row in reader:

            for field in row:

                if field == finder:

                    return True

    return False


def MultipleIsInFile(file, params):

    out = list()

    for param in params:

        if not IsInFile(file, param):

            out.append(param)

    return out


def DataFinder(soup, params):
    out = list()

    for param in params:

        try:

            if soup.find(text=re.compile(param)) is not None:

                out.append(soup.find(text=re.compile(param)))

        except:

            continue

    return out
