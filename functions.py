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


def DistinctList(list):

    checked = []

    for element in list:

        if element not in checked and element:

            checked.append(element)

    return checked


def OutputCollector(params, soup, output_list):

    params_out = DataFinder(soup, params)

    params_out = DistinctList(params_out)

    if params_out:

        for param_out in params_out:

            if not IsInFile("data.csv", param_out):

                output_list.append(param_out)

    return output_list
