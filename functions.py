import re


def IsInFile(file, finder):
    try:
        checkFile = open(file, "r")
        if checkFile.read().find(finder):
            return True
        else:
            return False
    except:
        return False


def DataFinder(soup, params):
    out = list()

    for param in params:

        try:
            if soup.find(text=re.compile(param)) is not None:
                out.append(soup.find(text=re.compile(param)))
        except:
            out.append("")
            continue

    return out
