import re
from files import FileHandler


class Regex():

    def searchImprints(self, input):
        fh = FileHandler()
        for key in fh.readImprintKeys():
            regex = re.compile(str(key))
            return regex.findall(input)

    def searchData(self, input):
        fh = FileHandler()
        for regex_input in fh.readRegex():
            regex = re.compile(regex_input)
            return regex.findall(input)
