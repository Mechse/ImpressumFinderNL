import re
import csv


def IsInFile(file, finders):

    try:

        with open(file, "r") as f:

            reader = csv.reader(f, delimeter=",")

            for row in reader:

                for field in row:

                    for finder in finders:

                        if field == finder:

                            return False

        return True
    except:
        return False


def DataFinder(soup, params):
    out = list()

    for param in params:

        try:

            if soup.find(text=re.compile(param)) is not None:

                out.append(soup.find(text=re.compile(param)))

        except:

            continue

    return out
