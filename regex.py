import re
from files import FileHandler


class Regex():

    def searchImprints(self, input):
        fh = FileHandler()
        for key in fh.readImprintKeys():
            regex = re.compile(str(key))
            return regex.findall(input)
