
class FileHandler():

    def readImprintKeys(self, filename="imprintKeys.txt"):
        try:
            file = open(str(filename), "r")
        except IOError:
            return str(filename) + " not found"

        output = file.read().splitlines()

        file.close()
        return output

    def writeImprintKeys(self, input, filename="imprintKeys.txt"):
        try:
            file = open(str(filename), "a")
        except IOError:
            return str(filename) + " not found"
        file.write(input)
        file.close()
        return

    def readImprintsFound(self, filename="imprintsFound.txt"):
        try:
            file = open(str(filename), "r")
        except IOError:
            return str(filename) + " not found"

        output = list()
        for i in file.readlines():
            output.append(i)

        file.close()
        return output

    def writeImprintsFound(self, input, filename="imprintsFound.txt"):
        try:
            file = open(str(filename), "a")
        except IOError:
            return str(filename) + " not found"
        file.write(input)
        file.close()
        return

    def readNothingFound(self, filename="nothingFound.txt"):
        try:
            file = open(str(filename), "r")
        except IOError:
            return str(filename) + " not found"

        output = list()
        for i in file.readlines():
            output.append(i)

        file.close()
        return output

    def writeNothingFound(self, input, filename="nothingFound.txt"):
        try:
            file = open(str(filename), "a")
        except IOError:
            return str(filename) + " not found"
        file.write(input)
        file.close()
        return

    def readSomethingFound(self, filename="somethingFound.txt"):
        try:
            file = open(str(filename), "r")
        except IOError:
            return str(filename) + " not found"

        output = list()
        for i in file.readlines():
            output.append(i)

        file.close()
        return output

    def writeSomethingFound(self, input, filename="somethingFound.txt"):
        try:
            file = open(str(filename), "a")
        except IOError:
            return str(filename) + " not found"
        file.write(input)
        file.close()
        return

    def readRegex(self, filename="regex.txt"):
        try:
            file = open(str(filename), "r")
        except IOError:
            return str(filename) + " not found"

        output = list()
        for i in file.readlines():
            output.append(i)

        file.close()
        return output

    def writeRegex(self, input, filename="regex.txt"):
        try:
            file = open(str(filename), "a")
        except IOError:
            return str(filename) + " not found"
        output = file.read()
        file.close()
        return output
